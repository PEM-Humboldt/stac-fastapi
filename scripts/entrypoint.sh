#!/bin/bash
set -e

if [ "${RUN_MIGRATIONS}" = "true" ]; then
    echo "Running PGStac migrations..."
    echo pypgstac migrate --dsn "postgresql://${POSTGRES_USER}:${POSTGRES_PASS}@${POSTGRES_HOST_WRITER}:${POSTGRES_PORT}/${POSTGRES_DBNAME}"
    pypgstac migrate --dsn "postgresql://${POSTGRES_USER}:${POSTGRES_PASS}@${POSTGRES_HOST_WRITER}:${POSTGRES_PORT}/${POSTGRES_DBNAME}"
    echo "Migrations complete."
fi

exec python -m stac_fastapi.pgstac.app
