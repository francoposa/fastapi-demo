from typing import Mapping

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float

demo_items_db = {
    "item-a": Item(name="item-a", price=5.99),
    "item-b": Item(name="item-b", price=14.99),
}

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_item(item: Item) -> Item:
    existing_item = demo_items_db.get(item.name)
    if existing_item is not None:
        raise HTTPException(status_code=409, detail="Item already exists")
    demo_items_db[item.name] = item
    return demo_items_db[item.name]


@router.get("/{item_id}")
async def get_item(item_id: str) -> Item:
    item = demo_items_db[item_id]
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/")
async def list_items() -> Mapping[str, Item]:
    return demo_items_db
