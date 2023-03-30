from fastapi import FastAPI
from dataclasses import dataclass
from backend.schema import BookSchema


app = FastAPI()



@app.get('/', status_code=200)
@app.get('/ping', status_code=200)
@app.post('/ping', status_code=200)
async def healthchk():
    return {'status_code': 200, 'detail': 'OK'}


# raise HTTPException(status_code=404, detail="Book not found.")







