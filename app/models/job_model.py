from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from beanie import Document
from bson import ObjectId

class Job(Document):
    job_id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    posted_at: datetime = Field(default_factory=datetime.utcnow)
    updated_posted_at: datetime = Field(default_factory=datetime.utcnow)
    admin_id: ObjectId

    class Settings:
        collection = "jobs"