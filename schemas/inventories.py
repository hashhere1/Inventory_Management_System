from pydantic import BaseModel
from typing import Optional

class CreateInventory(BaseModel):
    product_id: int
    quantity: int

class UpdateInventory(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None