import pygame
import sys
from math import log, log2
import colorsys

MAX_ITER = 255

def mandlebrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    if n == MAX_ITER:
        return MAX_ITER
    return n + 1 - log(log2(abs(z)))

def handle_clicks(event):
    global RE_END
    global RE_START
    global IM_END
    global IM_START
    click_x = event.pos[0]
    click_y = event.pos[1]
    small_y = SCREEN_HEIGHT / 3
    small_x = SCREEN_WIDTH / 3
    tmp_rs = RE_START
    tmp_re = RE_END
    tmp_is = IM_START
    tmp_ie = IM_END
    RE_START = tmp_rs + ((click_x - (small_x / 2)) / SCREEN_WIDTH) * (tmp_re - tmp_rs)
    RE_END = tmp_rs + ((click_x + (small_x / 2)) / SCREEN_WIDTH) * (tmp_re - tmp_rs)
    IM_START = tmp_is + ((click_y - (small_y / 2)) / SCREEN_HEIGHT) * (tmp_ie - tmp_is)
    IM_END = tmp_is + ((click_y + (small_y / 2)) / SCREEN_HEIGHT) * (tmp_ie - tmp_is)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the left button is pressed
            if event.button == 1:
                handle_clicks(event)
                fractal.fill((0, 0, 0))
                draw_mandlebrot()
                return


def draw_mandlebrot():
    global RE_END
    global RE_START
    global IM_END
    global IM_START
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            check_events()
            c = complex(RE_START + (x / SCREEN_WIDTH) * (RE_END - RE_START), IM_START + (y / SCREEN_HEIGHT) * (IM_END - IM_START))
            m = mandlebrot(c)
            hue = 0
            saturation = 0
            value = int(100 * m / MAX_ITER)
            hsva = (hue, saturation, value, 100)
            c = pygame.Color(0,0,0)
            c.hsva = hsva
            fractal.set_at([x, y], c)
            pygame.display.flip()
        screen.blit(fractal, (0, 0))


# Plot coords
RE_START = -2  # Left
RE_END = 1  # Right
IM_START = -1  # Down
IM_END = 1  # Up

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Als je dit leest ben je een beta")

fractal = screen.copy()
pygame.mixer.init()

fractal.fill((0, 0, 0))
draw_mandlebrot()
running = True

while running:
    check_events()

