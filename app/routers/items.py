from fastapi import APIRouter, HTTPException, Depends, Response
from app import models, database
from sqlmodel import Session
from typing import List

router = APIRouter()

@router.get("/items/{item_id}", response_model=models.Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    item = db.get(models.Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/", response_model=List[models.Item])
def read_items(db: Session = Depends(database.get_db)):
    items = db.query(models.Item).all()
    return items

@router.post("/items/", response_model=models.Item)
def create_item(item: models.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = models.Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    item = db.get(models.Item, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return Response(status_code=204)

