from fastapi import FastAPI
import uvicorn
from dataclasses import dataclass
from schema import BookSchema
from system import Seriescatalog , server

app = FastAPI()

def Login(id, password):
    for i in server.admin:
        if i.id == id and i.password == password:
            return True
    for i in server.customer:
        if i.id == id and i.password == password:
            return True
    return False

print(Login("admin", "admin"))

# @app.get('/', status_code=200)
# @app.get('/ping', status_code=200)
# @app.post('/ping', status_code=200)
# async def healthchk():
#     return {'status_code': 200, 'detail': 'OK'}

