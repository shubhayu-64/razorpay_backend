from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    amount: int
    receipt: str