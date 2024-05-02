from pydantic import BaseModel, EmailStr
from datetime import datetime

class BlogIn(BaseModel):
    title: str
    description: str
    created_by: EmailStr

class Blog(BlogIn):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
