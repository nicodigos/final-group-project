from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionBase(BaseModel):
    amount: float
    date: date
    category: str
    type: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
