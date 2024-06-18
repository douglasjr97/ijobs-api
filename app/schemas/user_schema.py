from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description='User E-mail')
    username: str = Field(
        ...,
        min_length=5,
        max_length=50,
        description='Username'
    )
    password: str = Field(
        ...,
        min_length=5,
        max_length=50,
        description='User Password'
    )
    
class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: str