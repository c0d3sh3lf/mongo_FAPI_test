from fastapi import FastAPI, Request
from app.database import get_db
from app.models import Items
from app.schema import ItemSchema

db = get_db()
app = FastAPI()

@app.get("/")
def index(request: Request):
    return {"success": "You made it work!"}

@app.get("/items")
def get_all_items(request: Request):
    all_items = []
    for item in Items.objects:
        all_items.append(item.__dict__())
    return all_items

@app.get("/items/{id}")
def get_item_by_id(request: Request, id: str):
    item = Items.objects(id=id).first()
    return item.__dict__()

@app.post("/items")
def add_item(request: Request, details: ItemSchema):
    profit = (details.selling_price - details.cost_price) * details.quantity
    item = Items(
        name=details.name,
        description = details.description,
        quantity = details.quantity,
        cost_price = details.cost_price,
        selling_price = details.selling_price,
        profit = profit
    )
    item.save()
    return item.__dict__()

@app.put("/items/{id}")
def add_item(request: Request, details: ItemSchema, id: str):
    profit = (details.selling_price - details.cost_price) * details.quantity
    item = Items.objects(id=id).first()
    item.update(
        name = details.name,
        description = details.description,
        quantity = details.quantity,
        cost_price = details.cost_price,
        selling_price = details.selling_price,
        profit = profit
    )
    item.save()
    return item.__dict__()

@app.delete("/items/{id}")
def delete_item(request: Request, id: str):
    item = Items.objects(id=id)
    item.delete()
    return {"success": f"item with id {id} deleted"}