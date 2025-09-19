from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def hello_world():
    return "Hello World!"

@app.get("/api/v1/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

@app.post("/api/v1/items/")
async def create_item(item: Item):
    return (f"El item {item.name} es {item.description}, cuesta {item.price}, y tiene un impuesto de {item.tax}")