from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse

from src.carriers.handler import carrier_handler

router = APIRouter()
from ..main import templates  # noqa: E402


@router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'carriers': carrier_handler.carriers})


@router.post('/track', response_class=JSONResponse)
async def track_package(carrier_name: str = Form(...), tracking_number: str = Form(...)):
    track_data = None
    if carrier := carrier_handler.carriers.get(carrier_name):
        track_data = carrier.track(track_number=tracking_number)
    if track_data is None:
        track_data = {'error': f'Carrier {carrier} not supported yet'}
    return track_data
