FROM python:3.11-slim as base

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

FROM base as builder

WORKDIR /app

COPY . /app

RUN python -m pip install /app/stac_fastapi/types \
                          /app/stac_fastapi/api \
                          /app/stac_fastapi/extensions

RUN python -m pip install --no-deps stac-fastapi.pgstac==3.0.0

RUN python -m pip install -r /app/requirements.pgstac.txt

RUN python -m pip install uvicorn
