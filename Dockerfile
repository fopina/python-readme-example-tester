FROM python:3.10-alpine AS base

# --- builder
FROM base AS builder
WORKDIR /app
RUN pip install uv
COPY readme_tester /src/readme_tester
COPY pyproject.toml README.md /src/
RUN uv pip install --target=/app /src

# --- main
FROM base
COPY --from=builder /app /app
ENV PYTHONPATH=/app

ENTRYPOINT ["python3", "-m", "readme_tester"]
