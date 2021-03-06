from typing import Optional, List
from enum import Enum

from fastapi import FastAPI, Query, Body, status as Status, HTTPException, Header
from pydantic import BaseModel, Field


app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    price: float = Field(
        ...,
        gt=0,
        description="The price must be greater than zero",
        title="The price of the item",
    )
    is_offer: Optional[bool] = None
    image: Optional[Image] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


items = {"foo": "The Foo Wrestlers"}


@app.get("/")
def read_root(
    user_agent: Optional[str] = Header(None),
    strange_header: Optional[str] = Header(None, convert_underscores=False),
    x_token: Optional[List[str]] = Header(None),
):
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
    if item_id not in items:
        raise HTTPException(
            status_code=Status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$"),
    q2: str = Query(
        ...,
        min_length=3,
        alias="item-query",
        deprecated=True,
    ),  # needly & alias not valid python var & deprecated
):
    """put data
    * If the parameter is also declared in the path, it will be used as a path parameter.
    * If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
    *If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body."""
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """Enum"""
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.put("/items/{item_id}/2")
async def update_item2(item_id: int, item: Item = Body(..., embed=True)):
    """
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        }
    }

    instead of

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
    """
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/{item_id}/1")
async def update_item1(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),
    q: Optional[str] = None
):
    """
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        },
        "importance": 5
    }
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


@app.post("/items/", status_code=Status.HTTP_201_CREATED)
async def create_item(name: str):
    return
