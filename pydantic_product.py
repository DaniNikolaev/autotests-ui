from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price should be greater than 0")
    tags: list[str] = []
    market: Market


product_data = {
    "name": "Beer",
    "price": 57.90,
    "tags": ["sales", "fresh"],
    "market": {"id": 1, "name": "K&B"}
}

product = Product(**product_data)
print(product)
