from typing import Optional
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
def read_root():
    """根路径"""
    return {"hello": "world"}


@app.get("/items/me")
async def read_item_me():
    """多路径匹配"""
    return {"id": "the current id"}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(item_id: str, user_id: int, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """查询可选参数"""
    return {"id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """PUT data"""
    return {"id": item_id, "name": item.name, "price": item.price}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """Enum"""
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
