from fastapi import Form, Request
from fastapi.responses import HTMLResponse, JSONResponse

from src.carriers.handler import carrier_handler
from src.main import app, templates


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/track', response_class=JSONResponse)
async def track_package(carrier: str = Form(...), tracking_number: str = Form(...)):
    tracking_data = carrier_handler.track(carrier=carrier, tracking_number=tracking_number)
    if tracking_data is None:
        tracking_data = {'error': f'Carrier {carrier} not supported yet'}

    return tracking_data
