from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    username: str
    password: str
    role: str

class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None