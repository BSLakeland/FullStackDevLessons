from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import os
app = FastAPI()

@app.get("/time", response_class=HTMLResponse)
async def homepage():
    time = datetime.now()
    message = f"the time is {time}"
    os.system(f"say '{message}'")
    return f"<h1>{message}</h1>"

@app.get('/hello/{name}', response_class=HTMLResponse)
async def hello_name(name: str):
    return f'<h1>Hello {name}</h1>'