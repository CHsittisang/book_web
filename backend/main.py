from fastapi import FastAPI , Request 
from dataclasses import dataclass , field
from backend.schema import BookSchema , AccountSchema , LoginSchema
from backend.book import Book_catalog
from backend.system import System , server ,customer ,system
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

app = FastAPI()
router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")

@app.get("/register")
async def show_form(request: Request):
    return templates.TemplateResponse("register_form.html", {"request": request})

@app.post('/register', status_code=200)
async def register(account: AccountSchema):
    system.add_customer(account)
    return {"message": f"Successfully registered {account.name}"}


@app.post('/login', status_code=200)
async def login(Login: LoginSchema):
    for i in system.customer:
        if i.id == Login.id and i.password == Login.password:
            return {"message": f"Successfully login {i.name}"}
    return {"message": f"login fail"}
