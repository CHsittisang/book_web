from typing import Optional , List
from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    id : str
    password: str
    email: str
    name: str
    phone: str


class BookSchema(BaseModel):
    catalog_name: str
    detail_series: str
    type: str
    tag: str
    img: str
    releae_date: str


  
class SeriesSchema(BaseModel):
    last_Update: str
    series_name: str
    imagre: str
    
    
class LoginSchema(BaseModel):
    id: str
    password: str
    
    

    