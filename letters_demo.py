import picounicorn
import time

R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
X = R
O = [0, 0, 0]
Y = [255, 180, 0]
letters = {
    'A': [
        O, O, X, O, O,
        O, X, O, X, O,
        O, X, X, X, O,
        O, X, O, X, O,
        O, X, O, X, O,
    ],
    'B': [
        O, X, X, O, O,
        O, X, O, X, O,
        O, X, X, O, O,        
        O, X, O, X, O,        
        O, X, X, O, O,        
    ],
    'C': [
        O, O, X, X, O,
        O, X, O, O, O,
        O, X, O, O, O,
        O, X, O, O, O,
        O, O, X, X, O,        
    ],
    'H': [
        O, X, O, X, O,
        O, X, O, X, O,
        O, X, X, X, O,
        O, X, O, X, O,
        O, X, O, X, O,        
    ],
    'W': [
        X, O, X, O, X,
        X, O, X, O, X,
        X, O, X, O, X,
        X, O, X, O, X,
        O, X, O, X, O,        
    ],
    'a': [
        O, X, X, O, O,
        O, O, O, X, O,
        O, O, X, X, O,
        O, X, O, X, O,
        O, O, X, X, O,
    ],
    'b': [
        O, X, O, O, O,
        O, X, O, O, O,
        O, X, X, O, O,
        O, X, O, X, O,
        O, X, X, O, O,
    ],
    'c': [
        O, O, O, O, O,
        O, O, O, O, O,
        O, O, X, X, O,
        O, X, O, O, O,
        O, O, X, X, O,
    ],
    'd': [
        O, O, O, X, O,
        O, O, O, X, O,
        O, O, X, X, O,
        O, X, O, X, O,
        O, O, X, X, O,
    ],
    'e': [
        O, O, X, O, O,
        O, X, O, X, O,
        O, X, X, X, O,
        O, X, O, O, O,
        O, O, X, X, O,
    ],
    'l': [
        O, X, O, O, O,
        O, X, O, O, O,
        O, X, O, O, O,
        O, X, O, X, O,
        O, O, X, O, O,        
    ],
    'o': [
        O, O, O, O, O,
        O, O, O, O, O,
        O, O, X, O, O,
        O, X, O, X, O,
        O, O, X, O, O,
    ],
    'r': [
        O, X, O, O, O,
        O, X, X, X, O,
        O, X, O, O, O,
        O, X, O, O, O,
        O, X, O, O, O,
    ],
    ' ': [
        O, O, O, O, O,
        O, O, O, O, O,
        O, O, O, O, O,
        O, O, O, O, O,
        O, O, O, O, O,
    ]
}

alien = [
    O, G, G, G, O,
    G, R, G, R, G,
    G, G, G, G, G,
    B, B, B, B, B,
    B, O, B, O, B,
]

pman = [
    O, Y, Y, Y, O,
    Y, O, Y, Y, Y,
    Y, Y, Y, Y, O,
    Y, Y, Y, O, O,
    O, Y, Y, Y, O,    
]

def draw_image(x, y, image_data, w=5, h=5):
    dw = picounicorn.get_width()
    dh = picounicorn.get_height()
    for xi in range(5):
        if xi + x >= dw:
            return
        if xi + x < 0:
            continue
        for yi in range(5):
            if yi + y >= dh:
                break
            print(xi+x, yi+y)
            pixel = image_data[yi*h + xi]
            # We've inverted X Y here.            
            picounicorn.set_pixel(x + xi, y + yi, pixel[0], pixel[1], pixel[2])

picounicorn.init()
text = "Hello World"
while True:
    for offset in range(0, 5*len(text)):
        for pos, letter in enumerate(text):
            draw_image((pos * 5) - offset, 0, letters[letter])
        time.sleep(0.1)
