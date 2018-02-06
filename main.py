#!/usr/bin/env python3
import pygame, sys, time, math
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.mapengine import *
from scripts.NPC import *
from scripts.player import *
from scripts.meloontic_gui import *
from os import path
pygame.init()
window_width = 800
window_height = 600
cSec = 0
cFrame = 0
FPS = 0

clock = pygame.time.Clock()
deltatime = 0


fps_font = pygame.font.SysFont("Ubuntu Light", 20)
sky = pygame.image.load("./textures/daysky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky




logo_img_temp = pygame.image.load("./textures/daysky.png")
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp

game_folder = path.dirname(__file__)
map_folder = path.join(game_folder, 'maps')
maps = TiledMap(path.join(map_folder, 'map.tmx'))
map_img = maps.make_map()


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title, clock
    window_width, window_height = 800, 600
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    clock = pygame.time.Clock()

def count_fps():
    global FPS, deltatime
    FPS = clock.get_fps()
    if FPS > 0:
        deltatime = 1 / FPS


create_window()

player = Player("Mousie")
player_w, player_h = player.width, player.height
player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
player_y = ((window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)

#Initialize Music
pygame.mixer.music.load("./music/Music.wav")
pygame.mixer.music.play(-1)

#Initialize GUI
def Play():
    Globals.scene = "game"

def Exit():
    global isRunning
    isRunning = False

btnPlay = Menu.Button(text = "Play", rect = (0, 0, 300, 60), tag = ("menu", None))
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Command = Play

btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60), tag = ("menu", None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Welcome to the RPG", color = Color.BlanchedAlmond, font = Font.Large)
menuTitle.Left , menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0

logo = Menu.Image(bitmap = logo_img)

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:#Left click
                #Handle button click events
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()  #Do Button Event
                        btn.Rolling = False
                        break    #Exit Loop


    #RENDER SCENE
    if Globals.scene == "game":

    #LOGIC
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 100 * deltatime
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 100 * deltatime
        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 100 * deltatime
        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 100 * deltatime

        player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
        player_y = ((window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)






   #render graphics

        window.blit(Sky, (0, 0))
        window.blit(map_img, (Globals.camera_x, Globals.camera_y))
        player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))
    # PROCESS MENU

    elif Globals.scene == "menu":
        window.fill(Color.Fog)

        logo.Render(window)
        menuTitle.Render(window)
        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)


    show_fps()

    pygame.display.update()
    clock.tick()
    count_fps()



pygame.quit()
sys.exit()
