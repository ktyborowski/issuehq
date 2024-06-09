from flask import Flask
from issuehq.db import db
from flask_cors import CORS
from flask import json
from werkzeug.exceptions import HTTPException
from issuehq.collections import create_collections
from issuehq.collections import wclient
from flask import make_response
from functools import reduce
import operator
from flask import abort, make_response
from issuehq.models import Issue, Repository, Search
from playhouse.shortcuts import model_to_dict
from issuehq.tasks import fetch_issues
from issuehq.collections import wclient
from flask import request
import requests
import weaviate.classes as wvc
import os

app = Flask("IssueHQ")

CORS(app)


wclient.connect()
create_collections()


@app.before_request
def before_request():
    if db.is_closed():
        db.connect()


@app.after_request
def after_request(response):
    if not db.is_closed():
        db.close()

    return response


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return HTTP errors as JSON."""

    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@app.get("/health")
def health():
    """Check application health"""

    response = make_response("OK!", 200)
    response.mimetype = "text/plain"

    return response



@app.get("/repositories")
def get_repositories():
    """List all repositories"""

    repositories = Repository().select()
    repositories = [model_to_dict(repository) for repository in repositories]

    return repositories


@app.post("/repositories")
def create_repository():
    """Create a repository"""

    full_name = request.get_json().get("full_name")

    if not full_name:
        abort(400, description="full_name is required.")

    response = requests.get(
        f"https://api.github.com/repos/{full_name}",
        headers={"Authorization": f"Bearer {os.getenv('GITHUB_ACCESS_TOKEN')}"},
    )
    data = response.json()

    repository = Repository(
        name=data["name"],
        full_name=data["full_name"],
        description=data["description"],
        html_url=data["html_url"],
    )
    repository.save()

    fetch_issues(repository.id)

    return model_to_dict(repository)


@app.get("/repositories/<int:id>")
def get_repository(id: int):
    """Retrieve a repository"""

    repository = Repository().select().where(Repository.id == id).get()
    return model_to_dict(repository)


@app.get("/issues/search")
def get_issues():
    """List issues that belong to a repository"""

    query = request.args.get("query")
    mode = request.args.get("mode", "near_text")
    limit = int(request.args.get("limit", "15"))
    alpha = request.args.get("alpha")

    excludes = request.args.getlist("exclude")

    target = request.args.get("target")
    state = request.args.get("state", "all")

    if not target:
        abort(400, descriptions="Target is required.")

    if query:
        query_params = {"query": query, "limit": limit}
        if mode == "hybrid":
            query_params["alpha"] = float(alpha) if alpha else 0.0

        if mode == "bm25":
            query_params["query_properties"] = target.split("_")
        else:
            query_params["target_vector"] = target

        filters = None
        if excludes:
            excludes = [
                wvc.query.Filter.by_property("title").not_equal(exclude)
                for exclude in excludes
            ]

            filters = reduce(operator.and_, excludes)

        if state != "all":
            state_filter = wvc.query.Filter.by_property("state").equal(state)
            if filters:
                filters = filters & state_filter
            else:
                filters = state_filter

        query_params["filters"] = filters

        issues_collection = wclient.collections.get("Issue")

        try:
            query_func = getattr(issues_collection.query, mode)
        except AttributeError:
            abort(400, description="Unsupported query type.")

        response = query_func(**query_params)

        issues = [obj.properties for obj in response.objects]

        Search.create(
            query=query, mode=mode, limit=limit, alpha=alpha, result_count=len(issues)
        )
    else:
        return []

    return issues[:limit]


@app.get("/issues/<public_id>")
def get_issue(public_id: str):
    """Retrieve an issue"""

    issue = Issue().select().where(Issue.public_id == public_id).get()

    if not issue:
        abort(404)

    return model_to_dict(issue)


@app.get("/issues/<public_id>/summary")
def get_issue_summary(public_id: str):
    """Retrieve a summary of an issue"""

    model = request.args.get("model")

    issue = Issue().select().where(Issue.public_id == public_id).get()

    if not issue:
        abort(404)

    if model == "transformers":
        query = f"""
        {{
          Get {{
            Issue(
              where: {{
                path: ["public_id"],
                operator: Equal
                valueString: "{public_id}"
              }}
              limit: 2
            ) {{
              title
              _additional {{
                summary(
                  properties: ["body"],
                ) {{
                  property
                  result
                }}
              }}
            }}
          }}
        }}
        """

        result = wclient.graphql_raw_query(query)
        print("RES", result)
        content = result.get["Issue"][0]["_additional"]["summary"][0]["result"]
    elif model == "ollama":
        collection = wclient.collections.get("Issue")

        response = collection.generate.near_text(
            query="Feature",  # The model provider integration will automatically vectorize the query
            single_prompt="Summarize the following issue: {body}",
            target_vector="body",
            filters=wvc.query.Filter.by_property("public_id").equal(public_id),
            limit=1,
        )

        result = response.objects.pop()
        content = result.generated
    else:
        abort(400, description="Model is required.")

    return {"content": content}


@app.get("/issues/<public_id>/similar")
def get_similar_issues(public_id: str):
    """Retrieve similar issues"""

    issue = Issue().select().where(Issue.public_id == public_id).get()

    if not issue:
        abort(404)

    collection = wclient.collections.get("Issue")

    response = collection.query.near_object(
        near_object=issue.uuid,
        target_vector="body_title",
        limit=5,
    )

    return [obj.properties for obj in response.objects]


@app.get("/searches")
def get_searches():
    searches = Search().select().order_by(Search.created_at.desc())
    searches = [model_to_dict(search, recurse=False) for search in searches]

    return searches


@app.post("/issues/<public_id>/chat")
def chat(public_id: str):
    issue = Issue().select().where(Issue.public_id == public_id).get()

    if not issue:
        abort(404)

    data = request.get_json()

    if not "messages" in data:
        abort(400, "Messages are required.")

    req_data = {"model": "llama3", "messages": data["messages"], "stream": False}

    res = requests.post("http://localhost:7869/api/chat", json=req_data)
    res_data = res.json()

    return res_data["message"]
