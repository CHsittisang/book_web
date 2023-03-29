from typing import Optional
from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    id : str
    password: str
    email: str
    name: str
    phone: str


class BookSchema(BaseModel):
    book_name: str 
    type: str
    tag: str
    price: int
    releae_date: str
    suply: str
    author: str

    
class SeriesSchema(BaseModel):
    last_Update: str
    series_name: str
    imagre: str
    
    

    
    

    