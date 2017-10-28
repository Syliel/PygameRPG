#!/usr/bin/env python2
import pygame, sys, time
from scripts.UltraColor import *
from scripts.textures import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0


fps_font = pygame.font.SysFont("Ubuntu Light", 20)
sky = pygame.image.load("/home/syliel/pygamerpg/textures/daysky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")



create_window()
count_fps()
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    #LOGIC
    count_fps()



   #render graphics
    window.blit(Sky, (0, 0))

    # Render terrain
    for x in range(0, 640, Tiles.Size):
        for y in range(0, 480, Tiles.Size):
            window.blit(Tiles.Grass, (x, y))

    show_fps()

    pygame.display.update()

pygame.quit()
sys.exit()
