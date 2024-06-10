# issuehq
Advanced AI search across you GitHub Issues. Powered by Weaviate.

## Features

### GitHub import

Import issues directly from your GitHub repositories.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/import-demo.gif)

### Advanced search

Search issues by semantic meaning of the query, by keywords or both using the hybrid search.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/search-demo.gif)

### Filters and settings

Enchance your results with filters and settings. Exclude keywords, change the searched property or adjust the hybrid ratio.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/settings-filters-demo.gif)

### Query history

Easily return to your previous queries using the query history feature.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/history-demo.gif)


### Summarization

Summarize issues using transformers and ollama models.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/summary-demo.gif)

### Chat

Ask a chatbot more detailed questions about a specific issue.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/chat-demo.gif)


### Similar issues

Quicky identify the most similar issues.

![](https://github.com/ktyborowski/issuehq/blob/main/demos/similar-issues-demo.gif)

## Design

The app follows a typical backend/frontend architecture.

The components in the systems include:

- Backend (Flask)
- Frontend (Svelte)
- Vector database (Weaviate)
- LLM model service (Ollama)
- Vectorization service (Transformers)
- Summarization service (Transformers)

All of the components are orchestrated by docker compose.

Some persistent data, such as repositories, imported issues, search history, is stored in an sqlite database.

## Development

Follow these steps to run the project in development mode:

1. Add a GitHub access token environment variable: `export GITHUB_ACCESS_TOKEN=my-github-access-token`
2. Run the supporting services with docker compose: `docker compose up -d`
3. Install pipenv: `pip install -U pipenv`
4. Install the backend dependencies: `pipenv install`
5. Activate the python virtual environment
6. Start the backend server: `python -m flask --app issuehq.main run --debug`
7. Move to the frontend directory: `cd frontend`
8. Install frontend dependencies: `npm install`
9. Run the frontend server: `npm run dev`
10. Open the application at `http://localhost:5173/issues`
