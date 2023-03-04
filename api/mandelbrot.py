import numpy as np


def sample(c, max_iters):
    z=0
    n=0
    while abs(z) <=2 and n < max_iters:
        z = z*z + c
        n += 1
    if n == max_iters:
        return 0
    else:
        return n
    
    
def sample_area(real_start, real_end, imag_start, imag_end, max_iters, width, height):
    x = np.linspace(real_start, real_end, width)
    y = np.linspace(imag_start, imag_end, height)
    mandelbrot_set = np.empty((height, width))
    percent_complete = 0
    res = height * width
    for i in range(height):
        print(f"{percent_complete/res*100.0}% complete")
        for j in range(width):
            mandelbrot_set[i, j] = sample(x[j] + y[i] * 1j, max_iters)
            percent_complete += 1
    return mandelbrot_set


    

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return list(int(hex[i:i+2], 16) for i in (0, 2, 4))

def lerp_colour(col_a, col_b, t):
    r = int(col_a[0] + t * (col_b[0] - col_a[0]))
    g = int(col_a[1] + t * (col_b[1] - col_a[1]))
    b = int(col_a[2] + t * (col_b[2] - col_a[2]))
    return (r, g, b)

def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
