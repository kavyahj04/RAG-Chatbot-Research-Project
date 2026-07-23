# RAG Summer Project

A RAG + knowledge-graph chatbot over GitLab's security handbook.

- `rag/` — Python backend: chunking/embedding/graph-build scripts, plus a FastAPI app (`api.py`) that serves the existing `answer()` pipeline over HTTP.
- `frontend/` — React (Vite) chat UI that talks to the backend.

## Data pipeline (how it was built)

The source corpus is GitLab's security handbook (markdown files under `rag/security_doc/`).
It is turned into three aligned artifacts, all joined on a stable `chunk_id`
(`<relative_path>_<index>`, e.g. `gearing-ratios.md_0`).

**1. Chunking — `rag/pipeline/chunking.py` → `json/chunks.json`**
- Parses each markdown file by heading (h2–h6) so chunks respect section
  boundaries, carrying a heading "breadcrumb" as metadata.
- Targets ~500 tokens per chunk (`cl100k_base`), with 50-token overlap; oversized
  sections are split on paragraph boundaries.
- Generates a one-sentence retrieval summary per chunk with `gpt-4o-mini`
  (stored as `section_summary` for query-to-section matching).

**2. Embedding — `rag/pipeline/embed.py` → `json/embeddings.json`**
- `text-embedding-3-large`, 3072-dim, batched.
- Skips any chunk over 8,000 tokens (embedding-model input limit).

**3. Schema discovery — `rag/archive/` → `json/consolidated_schema.json`**
- `sampling_200.py` samples 200 relationship-dense chunks (keyword-guided).
- `discover_schema_200.py` runs an unconstrained `LLMGraphTransformer` pass to
  surface the raw entity/relationship vocabulary (`raw_extraction_200.json`).
- `consolidate_schema.py` merges near-duplicate types into a **frozen schema of
  26 node types and 39 relationship types**. This schema is then locked and used
  to constrain all downstream extraction.

**4. Graph extraction — `rag/pipeline/build_graph.py` → `json/graph_documents_full.jsonl`**
- LangChain `LLMGraphTransformer` with `gpt-4.1-mini`, constrained to the frozen
  schema plus handbook-specific extraction rules (e.g. extract Roles not people,
  formula-derived numbers become `DERIVED_FROM` edges).
- One JSONL record per chunk (`chunk_id`, `nodes`, `relationships`); resumable —
  reruns skip `chunk_id`s already written.

### Data artifacts (`rag/json/`)

| File | What it is | Records |
|---|---|---|
| `chunks.json` | text + heading/url/summary metadata | 4,343 |
| `embeddings.json` | `chunk_id` → 3072-dim vector | 4,343 |
| `consolidated_schema.json` | frozen graph schema | 26 nodes / 39 rels |
| `graph_documents_full.jsonl` | per-chunk extracted nodes & relationships | 4,343 |
| `graph_documents_clean.jsonl` | **Neo4j-ready** cleaned graph (see below) | 4,343 |

## Data quality (how it was analyzed & fixed)

Before loading into Neo4j the three artifacts were audited for consistency by
joining them on `chunk_id` and checking structural integrity:

- **Cross-file alignment** — confirmed 1:1 `chunk_id` coverage across chunks,
  embeddings, and graph docs.
- **Graph structure** — node/relationship counts, empty-extraction rate,
  orphan nodes, within-doc duplicate ids.
- **Dangling relationships** — edges whose `source`/`target` was never emitted as
  a node in the same document.
- **Schema conformance** — every node/relationship `type` checked against the
  frozen schema (case-insensitively).

**Issues found and fixed:**

1. **2 chunks had no embeddings** (`corporate/systems/_index.md_1` at 33,616 tok,
   `corporate/team/_index.md_1` at 9,866 tok). Root cause: the chunker refused to
   split any section containing raw HTML (`<table>`/`<div>`/`<ul>`), so these
   exceeded the 8,000-token embed limit and were skipped. **Fix — `rag/archive/test.py`:**
   strips the HTML to markdown (via `markdownify`) and re-splits only those two
   chunks into 55 properly-sized sub-chunks, then updates all three artifacts.
   Corpus went 4,290 → **4,343**, and all three files now align exactly.

2. **Node-type casing** — only ~41% of node types exactly matched the schema's
   Title Case (`"Asset or resource"` vs `"Asset or Resource"`); Neo4j labels are
   case-sensitive, so this would have created duplicate labels.

3. **1,034 dangling relationship endpoints** — would create phantom, typeless
   nodes on a naive `MERGE` load.

   Fixes 2 & 3 are applied by **`rag/pipeline/clean_graph.py`**, which reads
   `graph_documents_full.jsonl` (read-only) and writes a new
   `graph_documents_clean.jsonl`:
   - normalizes all node types to canonical Title Case (100% schema-conformant);
   - recovers 169 dangling endpoints whose type is known from elsewhere in the graph;
   - infers types for the remaining 505 unique endpoints with `gpt-4.1-mini`,
     constrained to the 26 schema types.

   Result: **0 dangling edges**, 100% canonical typing, all 18,804 relationships
   preserved, +737 recovered nodes (22,935 → 23,672).

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

## Pending

Data / knowledge graph:
- [ ] **Load into Neo4j** — ingest `graph_documents_clean.jsonl`, attaching each
      chunk's `embedding` (from `embeddings.json`) joined on `chunk_id`; add a
      vector index for retrieval. (`rag/pipeline/load-graph.py`)
- [ ] **Review the 505 LLM-inferred node types** in the clean file before trusting
      them in production — these are the only "guessed" values.
- [ ] **Fold the chunking fix back into `chunking.py`** — the HTML-strip logic
      currently lives only in `test.py`/`clean_graph.py`; `chunking.py` still has
      the old `<table>/<div>/<ul>` guard, so a full re-chunk would reintroduce the
      oversized-chunk bug.
- [ ] **Delete `rag/json/.bak_prefix/`** backups once the fixes are confirmed
      (the embeddings backup alone is ~272 MB).

Quality (optional, lower priority):
- [ ] ~25% of chunks produce no graph nodes/relationships — mostly link lists and
      nav fragments; confirm none are substantive.
- [ ] ~89% of nodes have empty `properties` — consider enriching if attribute-level
      retrieval is needed.

Retrieval / app:
- [ ] Wire the retriever (`rag/pipeline/retriever.py`, `query-decomposition.py`) to
      the Neo4j graph + vector index.
