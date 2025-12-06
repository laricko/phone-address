FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN pip install .

EXPOSE 8000

CMD ["uvicorn", "src.api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
