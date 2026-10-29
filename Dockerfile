# video2cua job image: run as an Azure Container Apps job (or AKS pod) next to
# the Foundry resource. The same image serves both commands:
#   docker run ... video2cua analyze /data/demo.mp4 --work /data/work/demo
#   docker run ... video2cua run /data/work/demo/runbook.json --start-url https://app.example
# Mount recordings and work directories at /data (e.g. an Azure Files share).
# BASE_IMAGE lets you build from a copy in your own registry (e.g. ACR).
ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE}

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Shared browser location, readable by the non-root user below.
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app
COPY pyproject.toml ./
COPY video2cua ./video2cua
RUN pip install --no-cache-dir ".[all]" \
    && playwright install --with-deps chromium

# Run as a non-root user; the agent drives a browser and should hold no extra rights.
RUN useradd --create-home v2c && mkdir -p /data && chown v2c /data
USER v2c
WORKDIR /data
ENTRYPOINT ["video2cua"]
CMD ["--help"]
