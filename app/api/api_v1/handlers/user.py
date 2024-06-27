from fastapi import APIRouter, HTTPException, status
import pymongo.errors
from schemas.user_schema import UserAuth, ResponseUserDetail
from services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post('/signup', summary='Create user', response_model=ResponseUserDetail)
async def signup(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
             status_code=status.HTTP_400_BAD_REQUEST,
             detail='The username or email of this user already exists.'
         )