from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from datetime import datetime
from pydantic import BaseModel
import os
import cv2
import numpy as np
from fastapi.staticfiles import StaticFiles

from . import settings
from . import mandelbrot

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
    
class SampleInput(BaseModel):
    real: float
    imag: float
    
@app.post("/sample")
async def sample(input: SampleInput):
    c = input.real + input.imag * 1j
    return mandelbrot.sample(c, 100)

class imageInput(BaseModel):
    real: float
    imag: float
    width: int
    height: int
    zoom: float
    max_iter: int
    
@app.post("/image")
async def image(input: imageInput):
    aspect_ratio = input.width / input.height
    
    width = input.width
    height = input.height
    
    real_start = input.real - input.zoom
    real_end = input.real + input.zoom
    imag_start = input.imag - (input.zoom * aspect_ratio)
    imag_end = input.imag + (input.zoom * aspect_ratio)
    
    mandelbrot_set = mandelbrot.sample_area(real_start, real_end, imag_start, imag_end, input.max_iter, height, width)
    # HACK: height and width are swapped
    print(mandelbrot_set.shape)
    # return

    hex_start = "#000000"
    hex_end = "#ffffff"
    
    rgb_start = mandelbrot.hex_to_rgb(hex_start)
    rgb_end = mandelbrot.hex_to_rgb(hex_end)
    
    rgb = np.zeros((width, height, 3), dtype=np.uint8)
    
    for i in range(width):
        for j in range(height):
            rgb[i, j] = mandelbrot.lerp_colour(rgb_start, rgb_end, mandelbrot_set[i, j] / input.max_iter)
            
    arr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    _success, im = cv2.imencode(".png", arr)
    headers = {"Content-Disposition": "'inline', 'filename':'image.png'"}
    return Response(im.tobytes(), headers=headers, media_type="image/png")