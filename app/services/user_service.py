from models.user_model import User
from schemas.user_schema import UserAuth
from typing import Optional
from uuid import UUID
from core.security import get_password

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user = User(
            username=user.username,
            email=user.email,
            hash_password=get_password(user.password)
        )
        
        await user.save()
        return user