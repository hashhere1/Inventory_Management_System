from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class CreateProduct(BaseModel):
    name: str
    description: str
    category_id: int
    supplier_id: int
    cost_price: Decimal
    selling_price: Decimal

class UpdateProduct(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    cost_price: Optional[Decimal] = None
    selling_price: Optional[Decimal] = None