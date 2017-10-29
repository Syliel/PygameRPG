#!/usr/bin/env python3
import pygame, sys, time
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
pygame.init()

cSec = 0
cFrame = 0
FPS = 0



clock = pygame.time.Clock()
deltatime = 0
MapEngine = Map_Engine()
terrain = MapEngine.load_map("/home/syliel/pygamerpg/test.map")

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
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1.0 / FPS



create_window()

player = Player("Mousie")
player_w, player_h = player.width, player.height
player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
player_y = ((window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)



count_fps()
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "west"
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0

    #LOGIC
    if Globals.camera_move == 1:
        Globals.camera_y += 100 * deltatime
    elif Globals.camera_move == 2:
        Globals.camera_y -= 100 * deltatime
    elif Globals.camera_move == 3:
        Globals.camera_x += 100 * deltatime
    elif Globals.camera_move == 4:
        Globals.camera_x -= 100 * deltatime

    player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
    player_y = ((window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)






   #render graphics
    window.blit(Sky, (0, 0))
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))
    # Render terrain


    show_fps()

    pygame.display.update()

    count_fps()


pygame.quit()
sys.exit()
