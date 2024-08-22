FROM python:3.11-slim as base

# Any python libraries that require system libraries to be installed will likely
# need the following packages in order to build
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

FROM base as builder

WORKDIR /app

COPY . /app

RUN python -m pip install stac-fastapi.types stac-fastapi.api stac-fastapi.extensions && \
    python -m pip install stac-fastapi.sqlalchemy && \
    python -m pip install stac-fastapi.pgstac

RUN pip install uvicorn
