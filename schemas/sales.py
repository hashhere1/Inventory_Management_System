from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class CreateSales(BaseModel):
    product_id: int
    quantity: int
    selling_price: Decimal
    user_id: int
    customer_name: str

class UpdateSale(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    selling_price: Optional[Decimal] = None
    user_id: Optional[int] = None
    customer_name: Optional[str] = None