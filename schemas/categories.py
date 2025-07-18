from pydantic import BaseModel
from typing import Optional

class CreateCategory(BaseModel):
    name: str
    description: str

class UpdateCategory(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None