from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from services.user_service import UserService
from schemas.auth_schema import tokenSchema
from core.security import create_access_token, create_refresh_token
from schemas.user_schema import ResponseUserAuth
from models.user_model import User
from typing import Any, Union
from api.dependecies.user_deps import get_current_user

auth_router = APIRouter()

@auth_router.post('/login', 
                  summary='Create access token and Refresh Token',
                  response_model=tokenSchema
                  )
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Union[str, Any]:
    user = await UserService.authenticate(
        email=data.username,
        password=data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email or Password is incorrect'
        )
        
    return {
             "access_token": create_access_token(user.user_id),
             "refresh_token": create_refresh_token(user.user_id)
    }
    
@auth_router.post('/test-token',
                  summary='Testing o token',
                  response_model=ResponseUserAuth)
async def test_token(user: User = Depends(get_current_user)):
    return user