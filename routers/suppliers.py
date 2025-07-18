from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from repository import supplier
import models
from database import get_db
from schemas import suppliers

router = APIRouter(
    tags=["Suppliers"],
    prefix="/suppliers"
)

@router.post("/create")
def create(request: suppliers.CreateSupplier, db: Session = Depends(get_db)):
    return supplier.create(request, db)

@router.get("/")
def show(db: Session = Depends(get_db)):
   return db.query(models.Suppliers).all()

@router.get("/by_id/{supplier_id}")
def show_by_id(supplier_id: int, db: Session = Depends(get_db)):
    return supplier.show_by_id(supplier_id, db)

@router.put("/update/{supplier_id}")
def update(supplier_id: int, request: suppliers.UpdateSupplier, db: Session = Depends(get_db)):
    return supplier.update(supplier_id, request, db)

@router.delete("/delete/{supplier_id}")
def delete(supplier_id: int, db: Session = Depends(get_db)):
    return supplier.delete(supplier_id, db)

