# STAC FAST-API IAvH

Este repsositorio es un fork de [stac-fastapi](https://github.com/stac-utils/stac-fastapi) creado por el Instituto de Investigación de Recursos Biológicos Alexander von Humboldt .

Utiliza Docker para la instalación del servidor. La creación del archivo [docker-compose-io.yml](docker-compose-io.yml) y las modificaciones al archivo [Dockerfile](Dockerfile) se basan en las configuraciones realizadas en el fork de stac-fastapi creado por [Biodiversite Quebec](https://github.com/BiodiversiteQuebec/stac-fastapi).

## Instalación

Seguir los siguientes pasos:

1. Construir la imagen de Docker para stac-fastapi.
    ````
    docker compose -f docker-compose-io.yml build
    ````

1. Levantar los contendores.
    ````
    docker compose -f docker-compose-io.yml up -d
    ````
