import pygame
import math
import numpy

W = 600
H = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption('Drawer')
clock = pygame.time.Clock()


def multiply(a, mult: float):
    rez = []
    for i in range(len(a)):
        rez.append(a[i] * mult)
    return rez


def mid_color(col1, col2):
    return col1[0] + col2[0] / 2, col1[1] + col2[1] / 2, col1[2] + col2[2] / 2


def fade(col1, col2, cnt):
    colorRange = []
    for i in range(cnt):
        colorRange.append(mid_color(multiply(col2, (i/cnt)**1), multiply(col1, 1 - (i/cnt)**1)))
    return colorRange


def fade_circle(surface, center, radius, col):
    new_surface = pygame.surface.Surface([2 * radius, 2 * radius])
    for i in reversed(range(0, radius, 1)):
        new_surface.fill(WHITE)
        new_surface.set_alpha(255 * (1 - i / len(range(0, radius)))**4)
        new_surface.set_colorkey(WHITE)
        pygame.draw.circle(new_surface, col, [radius, radius], i)
        screen.blit(new_surface, [center[0] - radius, center[1] - radius])


def circle(surface, center, radius, col):
    pygame.draw.circle(surface, col, center, radius)


screen.fill(WHITE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(300)
    mx, my = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed(3)[0]:
        fade_circle(screen, [mx, my], 25, BLACK)

    pygame.display.update()





