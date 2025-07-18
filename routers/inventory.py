from fastapi import APIRouter,Depends
from repository import inventory

import models
from database import get_db
from sqlalchemy.orm import Session
from schemas import inventories

router = APIRouter(
    tags=["Inventory"],
    prefix="/inventory"
)


@router.post("/create")
def create(request: inventories.CreateInventory, db: Session = Depends(get_db)):
    return inventory.create(request, db)

@router.get("/")
def show(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()

@router.get("/{inventory_id}")
def show_by_id(inventory_id: int, db: Session = Depends(get_db)):
    return inventory.show_by_id(inventory_id, db)

@router.put("/update/{inventory_id}")
def update(inventory_id: int, request: inventories.UpdateInventory, db: Session = Depends(get_db)):
    return inventory.update(inventory_id, request, db)

@router.delete("/delete/{inventory_id}")
def delete(inventory_id: int, db: Session = Depends(get_db)):
    return inventory.delete(inventory_id, db)