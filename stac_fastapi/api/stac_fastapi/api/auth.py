from datetime import datetime, timedelta, timezone
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from jose.exceptions import JWTClaimsError

from stac_fastapi.types.errors import UnauthorizedError
from stac_fastapi.types.config import ApiSettings

settings = ApiSettings()


auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@auth_router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.username != settings.user_username or form_data.password != settings.user_password:
        raise UnauthorizedError("Incorrect username or password")
    access_token = create_access_token(
        data={"sub": form_data.username}
    )
    return {"access_token": access_token}

def create_access_token(data: Dict[str, str]) -> str:
    expires_delta = timedelta(minutes=settings.access_token_expire_minutes)
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire.isoformat()})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        if payload is None:
            raise UnauthorizedError("Could not validate credentials")
        return payload
    except (JWTError,ExpiredSignatureError,JWTClaimsError) as e:
        raise UnauthorizedError(f"Error decoding token: {str(e)}")