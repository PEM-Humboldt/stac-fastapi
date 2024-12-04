from fastapi import FastAPI, Request ,HTTPException, status
from fastapi.security.utils import get_authorization_scheme_param
from stac_fastapi.api.auth import verify_token
from stac_fastapi.api.errors import UnauthorizedError

class AuthMiddleware:
    """
    Middleware to validate the token on all routes
    """
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive, send)
            path = scope.get("path", "")

            excluded_paths = ["/auth/token", "/docs", "/openapi.json"]
            if path not in excluded_paths:
                auth_header = request.headers.get("Authorization")
                if not auth_header:
                    raise UnauthorizedError("Authorization header missing")

                scheme, token = get_authorization_scheme_param(auth_header)
                if not token or scheme.lower() != "bearer":
                    raise UnauthorizedError("Invalid authentication scheme")

                try:
                    verify_token(token)
                except UnauthorizedError as e:
                    raise e

        await self.app(scope, receive, send)

