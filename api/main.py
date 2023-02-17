from fastapi import FastAPI
from datetime import datetime
import os
app = FastAPI()

@app.get("/")
async def homepage():
    time = datetime.now()
    message = f"the time is {time}"
    os.system(f"say '{message}'")
    return message

@app.get('/hello/{name}')
async def hello_name(name: str):
    return f'Hello {name}'