from pydantic import BaseModel
from typing import List, Optional

class PostSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class CreatePostSchema(BaseModel):
    userId: int
    title: str
    body: str

class UpdatePostSchema(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    userId: Optional[int] = None