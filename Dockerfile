# Usa la imagen de Python como base
FROM python:3.11-slim as base

# Instala dependencias del sistema
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Etapa de construcción
FROM base as builder

WORKDIR /app

# Copia todo el contenido del repositorio en el contenedor
COPY . /app

# Instala las dependencias locales
RUN python -m pip install /app/stac_fastapi/types \
                          /app/stac_fastapi/api \
                          /app/stac_fastapi/extensions

# Instala stac-fastapi.pgstac sin dependencias para evitar sobrescribir las versiones locales
RUN python -m pip install --no-deps stac-fastapi.pgstac

# Instala las demás dependencias desde requirements.txt
RUN python -m pip install -r /app/requirements.txt

# Instala Uvicorn
RUN python -m pip install uvicorn
