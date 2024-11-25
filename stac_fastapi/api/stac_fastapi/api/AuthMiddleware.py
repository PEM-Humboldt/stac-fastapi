from fastapi import FastAPI, Request ,HTTPException, status
from fastapi.security.utils import get_authorization_scheme_param
from stac_fastapi.api.auth import verify_token

class AuthMiddleware:
    """
    Middleware para validar el token en todas las rutas.
    """
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive, send)
            path = scope.get("path", "")
            method = request.method

            excluded_paths = ["/auth/token", "/docs", "/openapi.json"]
            if path not in excluded_paths:
                # Obtener token del header Authorization
                auth_header = request.headers.get("Authorization")
                if not auth_header:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Authorization header missing",
                        headers={"WWW-Authenticate": "Bearer"},
                    )

                scheme, token = get_authorization_scheme_param(auth_header)
                if not token or scheme.lower() != "bearer":
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid authentication scheme",
                        headers={"WWW-Authenticate": "Bearer"},
                    )

                try:
                    verify_token(token)
                except HTTPException as e:
                    raise e

        await self.app(scope, receive, send)

