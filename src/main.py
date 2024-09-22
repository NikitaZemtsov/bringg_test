import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from src.routers import track

app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.include_router(track.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
