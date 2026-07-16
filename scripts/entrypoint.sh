#!/bin/bash
set -e

if [ "${RUN_MIGRATIONS}" = "true" ]; then
    echo "Running PGStac migrations..."
    pypgstac migrate --dsn "postgresql://${POSTGRES_USER}:${POSTGRES_PASS}@${POSTGRES_HOST_WRITER}:${POSTGRES_PORT}/${POSTGRES_DBNAME}"
    echo "Migrations complete."
fi

exec uvicorn stac_fastapi.pgstac.app:app \
    --host "${APP_HOST:-0.0.0.0}" \
    --port "${APP_PORT:-8082}" \
    --workers "${WEB_CONCURRENCY:-1}" \
    --root-path "${ROOT_PATH:-}" \
    --proxy-headers \
    --forwarded-allow-ips="${FORWARDED_ALLOW_IPS:-*}"
