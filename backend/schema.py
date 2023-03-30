<<<<<<< HEAD
from typing import Optional , List
=======
from typing import Optional
>>>>>>> main
from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    id : str
    password: str
    email: str
    name: str
    phone: str


class BookSchema(BaseModel):
<<<<<<< HEAD
    catalog_name: str
    detail_series: str
    type: str
    tag: str
    img: str
    releae_date: str


  
=======
    book_name: str 
    type: str
    tag: str
    price: int
    releae_date: str
    suply: str
    author: str

    
>>>>>>> main
class SeriesSchema(BaseModel):
    last_Update: str
    series_name: str
    imagre: str
    
    
<<<<<<< HEAD
class LoginSchema(BaseModel):
    id: str
    password: str
    
    
=======
>>>>>>> main

    