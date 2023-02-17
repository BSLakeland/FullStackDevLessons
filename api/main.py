from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime
import os

from fastapi.staticfiles import StaticFiles

from . import settings

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request})

@app.get("/time", response_class=HTMLResponse)
async def timepage():
    time = datetime.now()
    message = f"the time is {time}"
    os.system(f"say '{message}'")
    return f"<h1>{message}</h1>"

@app.get('/hello/{name}', response_class=HTMLResponse)
async def hello_name(request: Request, name: str):
    return settings.TEMPLATES.TemplateResponse("homepage.html", {"request": request, "name": name})
    # return f'<h1>Hello {name}</h1>'