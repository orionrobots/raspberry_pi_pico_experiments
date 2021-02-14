import picounicorn
import time

picounicorn.init()

def set_all(r, g, b):
    w = picounicorn.get_width()
    h = picounicorn.get_height()
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, r, g, b)
        
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
pur = 255, 0, 255
yellow = 255, 255, 0

def get_pressed_button():
    if picounicorn.is_pressed(picounicorn.BUTTON_A):
        return True,picounicorn.BUTTON_A
    if picounicorn.is_pressed(picounicorn.BUTTON_B):
        return True, picounicorn.BUTTON_B
    if picounicorn.is_pressed(picounicorn.BUTTON_X):
        return True, picounicorn.BUTTON_X
    if picounicorn.is_pressed(picounicorn.BUTTON_Y):
        return True, picounicorn.BUTTON_Y
    return False, False
    
while True:
    pressed = None, None
    while not pressed[0]:
        pressed = get_pressed_button()
    button_colors = {
        picounicorn.BUTTON_A: red,
        picounicorn.BUTTON_B: green,
        picounicorn.BUTTON_X: blue,
        picounicorn.BUTTON_Y: yellow
    }
    
    set_all(*button_colors[pressed[1]])
    time.sleep(0.1)

