from pydantic import BaseModel


class Order(BaseModel):
    price: float
    quantity: int
    side: str  # "buy" or "sell"
    option: str  # "YES" or "NO"