from issuehq.models import Issue, Repository
from issuehq.collections import wclient
import requests
import re
from issuehq.db import db
from bs4 import BeautifulSoup
from markdown import markdown
from playhouse.shortcuts import model_to_dict

from huey import SqliteHuey

import os

huey = SqliteHuey("issuehq", filename="huey.db")

def markdown_to_plaintext(markdown_text):
    cleaned_text = re.sub(r"```.*?```", "", markdown_text, 0, re.DOTALL)
    html = markdown(cleaned_text)
    return "".join(BeautifulSoup(html, "lxml").find_all(string=True))


@huey.task()
def fetch_issues(repository_id):
    repository = Repository().select().where(Repository.id == repository_id).get()

    url = f"https://api.github.com/repos/{repository.full_name}/issues"

    pages_remaining = True
    while pages_remaining:
        response = requests.get(
            url,
            params={"per_page": 100},
            headers={"Authorization": f"Bearer {os.getenv('GITHUB_ACCESS_TOKEN')}"},
        )
        data = response.json()

        issues = [
            {
                "repository": repository.id,
                "title": issue["title"],
                "body": markdown_to_plaintext(issue["body"]) if issue["body"] else "",
                "number": issue["number"],
                "state": issue["state"],
                "html_url": issue["html_url"],
            }
            for issue in data
        ]

        with db.atomic():
            for issue in issues:
                Issue.create(**issue)

        link_header = response.headers.get("link")

        pages_remaining = link_header and 'rel="next"' in link_header

        if pages_remaining:
            regex = r"(?<=<)([\S]*)(?=>; rel=\"Next\")"
            url = re.search(regex, link_header, re.IGNORECASE).group()

    index_issues(repository.id)


@huey.task()
def index_issues(repository_id):
    wclient.connect()
    issues = Issue().select().where(Issue.repository == repository_id)
    issues = [model_to_dict(issue, recurse=False) for issue in issues]

    collection = wclient.collections.get("Issue")

    with collection.batch.dynamic() as batch:
        for issue in issues:
            issue.pop("id")
            batch.add_object(properties=issue, uuid=issue["uuid"])

    if wclient.is_connected():
        wclient.close()
