# RAG Summer Project

A RAG + knowledge-graph chatbot over GitLab's security handbook.

- `rag/` — Python backend: chunking/embedding/graph-build scripts, plus a FastAPI app (`api.py`) that serves the existing `answer()` pipeline over HTTP.
- `frontend/` — React (Vite) chat UI that talks to the backend.

## Backend (`rag/`)

```bash
cd rag
python3 -m venv venv          # already done; recreate if you move this folder again
source venv/bin/activate
pip install -r requirements.txt
```

Create `rag/.env` with:

```
OPENAI_API_KEY=sk-...
ALLOWED_ORIGINS=http://localhost:5173   # comma-separated list; set to your deployed frontend URL in prod
```

Run it:

```bash
uvicorn api:app --reload --port 8000
```

Endpoints:
- `GET /api/health`
- `POST /api/chat` — body `{"message": "..."}`, returns `{"answer": "...", "sources": [...]}`

A `Dockerfile` is included for deploying to any container host (Render, Railway, Fly.io, etc.). Whatever host you pick, it needs **persistent disk** (not classic stateless serverless) since `chroma_db/` and `graph.pkl` are loaded from local files on startup — that's why this isn't deployed as a Vercel serverless function.

> Note: this project was moved from another folder, which broke the old `venv`'s shebang paths (`pip`/`python` pointed at the old absolute path) — it's been recreated fresh. If you move the project again, recreate `venv/` rather than copying it.

## Frontend (`frontend/`)

```bash
cd frontend
npm install
cp .env.example .env.local   # set VITE_API_URL to your backend URL
npm run dev
```

### Deploying to Vercel

1. Push this repo to GitHub.
2. In Vercel, import the repo and set **Root Directory** to `frontend`.
3. Framework preset: Vite (auto-detected).
4. Add an environment variable `VITE_API_URL` pointing at your deployed backend (e.g. `https://your-backend.onrender.com`).
5. Deploy.

Make sure the backend's `ALLOWED_ORIGINS` includes your Vercel domain.
