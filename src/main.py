from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=str(Path(__file__).parent / 'templates'))

from src.routers import track  # noqa: E402

app.include_router(track.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
