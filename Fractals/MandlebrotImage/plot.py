from PIL import Image, ImageDraw
from mandlebrot import MAX_ITER, mandlebrot

# Frame size (px)
WIDTH = 1000
HEIGHT = 600


# # Plot coords
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1



palette = []

im = Image.new('HSV', (WIDTH, HEIGHT), (0,0,0))
draw = ImageDraw.Draw(im)

# Draws a basic mandelbrot image
for x in range(0, WIDTH):
    print(f"{x / WIDTH * 100}%")
    for y in range(0, HEIGHT):
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                  IM_START + (y / HEIGHT) * (IM_END - IM_START))
        m = mandlebrot(c)
        hue = int(m)
        saturation = int(m * 255 / MAX_ITER)
        value = 255 if m < MAX_ITER else 0
        draw.point([x,y], (hue, saturation, value))


im.convert('RGB').save('test.png', "PNG")
im.show()