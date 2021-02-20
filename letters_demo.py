import picounicorn

X = [255, 0, 0]
O = [0, 0, 0]

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
    ]    
}

def draw_image(x, y, image_data, w=5, h=5):

    for xi in range(5):
        for yi in range(5):
            print(xi, yi)
            pixel = image_data[yi*h + xi]
            # We've inverted X Y here.            
            picounicorn.set_pixel(x + xi, y + yi, pixel[0], pixel[1], pixel[2])

picounicorn.init()
draw_image(0, 0, letters['A'])
draw_image(5, 0, letters['B'])
