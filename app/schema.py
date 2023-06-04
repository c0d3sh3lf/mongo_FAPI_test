from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    description: str
    quantity: int
    cost_price: float
    selling_price: float