# STAC FAST-API IAvH

Este repsositorio es un fork de [stac-fastapi](https://github.com/stac-utils/stac-fastapi) creado por el Instituto de Investigación de Recursos Biológicos Alexander von Humboldt .

Utiliza Docker para la instalación del servidor. La creación del archivo [docker-compose-io.yml](docker-compose-io.yml) y las modificaciones al archivo [Dockerfile](Dockerfile) se basan en las configuraciones realizadas en el fork de stac-fastapi creado por [Biodiversite Quebec](https://github.com/BiodiversiteQuebec/stac-fastapi).

## Instalación

Seguir los siguientes pasos:

1. Crear un archivo .env réplica de env.sample y actualizar los valores de la variables de entorno.
    ```
    PGUSER="" # Usuario de la base de datos
    PGPASSWORD="" # Contraseña para el usuario de base de datos
    PGDATABASE="" # Nombre de la base de datos
    SECRET_KEY = "" # Llave secreta para validar el token
    ALGORITHM = "" # Algoritmo de firma utilizado para generar y verificar tokens , generalmente se usa este: "HS256"
    USER_USERNAME = "" # Usuario utilizado para la autenticacion
    USER_PASSWORD = "" # Contraseña utilizado para la autenticacion
    ACCESS_TOKEN_EXPIRE_MINUTES = # Tiempo en minutos para la expiración del token
    ```
   Nota: Para generar la llave secreta es necesario ejecutar esto en CMD o terminal de linux, adicional de tener una version de Python mayor a 3.6 instalada:
   
   ```
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

1. Construir la imagen de Docker para stac-fastapi.
    ````
    docker compose -f docker-compose-io.yml build
    ````

1. Levantar los contendores.
    ````
    docker compose -f docker-compose-io.yml up -d
    ````

1. Comprobar el funcionamiento correcto del servirdor: http://localhost:8082
