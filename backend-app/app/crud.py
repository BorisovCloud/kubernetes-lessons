"""CRUD operations for database models."""
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas


def get_item(db: Session, item_id: int) -> Optional[models.Item]:
    """Get a single item by ID."""
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    """Get a list of items with pagination."""
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_items_count(db: Session) -> int:
    """Get total count of items."""
    return db.query(func.count(models.Item.id)).scalar()


def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    """Create a new item."""
    db_item = models.Item(
        name=item.name,
        description=item.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: schemas.ItemUpdate) -> Optional[models.Item]:
    """Update an existing item."""
    db_item = get_item(db, item_id)
    if db_item is None:
        return None
    
    # Update only provided fields
    update_data = item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> bool:
    """Delete an item."""
    db_item = get_item(db, item_id)
    if db_item is None:
        return False
    
    db.delete(db_item)
    db.commit()
    return True
