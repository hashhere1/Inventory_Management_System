from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import sale
import models
from schemas import sales
from database import get_db
from auth.oauth2 import get_current_user

router = APIRouter(
    tags=["Sales"],
    prefix="/sales",
    dependencies=[Depends(get_current_user)]
)


@router.post("/create")
def create(request: sales.CreateSales, db: Session = Depends(get_db)):
    return sale.create(request, db)

@router.get("/")
def show(db: Session = Depends(get_db)):
    return db.query(models.Sales).all()

@router.get("/{sales_id}")
def show_by_id(sales_id: int, db: Session = Depends(get_db)):
    return sale.show_by_id(sales_id, db)

@router.put("/update/{sale_id}")
def update(sale_id: int, request: sales.UpdateSale, db: Session = Depends(get_db)):
    return sale.update(sale_id, request, db)

@router.delete("/delete/{sale_id}")
def delete(sale_id: int, db: Session = Depends(get_db)):
    return sale.delete(sale_id, db)

