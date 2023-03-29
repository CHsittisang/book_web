from fastapi import FastAPI
from dataclasses import dataclass
from backend.schema import BookSchema


app = FastAPI()


@dataclass
class Account: 
    id: str
    password: str 
    name: str 
    email: str 
    phone: str
        
@dataclass
class Book:
    book_name: str
    type: str
    tag: str
    price: int
    releae_date: str
    suply: str
    author: str
    
    
@dataclass
class Series_Catalog:
    last_Update: str
    series_name: str
    imagre: str

# create a list of books

book_list = []
all_series = []

@app.get("/all_series")
async def all_series():
    return print(book_list)

@app.post("/add_series")
async def add_series(last_Update: str, series_name: str, imagre: str):
    series_name = {
        "last_Update": last_Update,
        "imagre": imagre
    }
    all_series.append(series_name)
    return {"message": "Add series successful!" + " Series name:" + series_name + " Series last update:" + last_Update + " Series imagre:" + imagre}
        
@app.post("/add_book")
async def add_book(book: BookSchema):
    book_list.append(book)
    return {"message": "Add book successful!" }


@app.get('/', status_code=200)
@app.get('/ping', status_code=200)
@app.post('/ping', status_code=200)
async def healthchk():
    return {'status_code': 200, 'detail': 'OK'}


# raise HTTPException(status_code=404, detail="Book not found.")







