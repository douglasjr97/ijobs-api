from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

password_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def get_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else: 
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    inform_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }
    
    jwt_encoded = jwt.encode(
        inform_jwt,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )
    
    return jwt_encoded

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    inform_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }
    
    jwt_encoded = jwt.encode(
        inform_jwt,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )
    
    return jwt_encoded