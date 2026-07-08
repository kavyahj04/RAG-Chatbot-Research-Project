FROM python:3.13-slim

WORKDIR /app

COPY rag/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY rag/ .

ENV PORT=8000
EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
