from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]



class ProductCreate(BaseModel):
    name: str
    price: float


class ProductUpdate(ProductBase):
    id: int
    pass


class ProductResponse(ProductBase):
    created_at: datetime
    updated_at: Optional[datetime]
    class Config:
        orm_mode = True
