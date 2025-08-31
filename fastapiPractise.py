from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hii ! people"
           , "card":"Hi there "}

#You can declare the type of a path parameter in the function, using standard Python type annotations:
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


from pydanticPract import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None




@app.post("/items/")
async def create_item(item: Item):
    return item

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}