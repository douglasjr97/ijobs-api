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
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description='Name'
    )
    last_name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description='Last name'
    )
    address: str = Field(
        ...,
        min_length=5,
        max_length=50,
        description='Address'
    )
    
class ResponseUserDetail(BaseModel):
    user_id: UUID
    username: str
    email: str
    first_name: str
    last_name: str
    address: str
    
class ResponseUserAuth(BaseModel):
    user_id: UUID
    username: str
    email: str