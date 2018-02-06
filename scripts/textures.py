#!/usr/bin/env python3
import pygame
from scripts.UltraColor import *

pygame.init()

class Tiles:
    Size = 32

    Blocked = []
    Blocked_Types = ["3"]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False


    def Load_Texture(file, posx, posy, width, height):
        bitmap = pygame.image.load(file)
        image = pygame.Surface([width, height], pygame.HWSURFACE|pygame.SRCALPHA)
        image.blit(bitmap, (0, 0), (posx, posy, width, height))
        image.set_colorkey(Color.Black)
        return image



    Grass = Load_Texture("./textures/Grass2.png", 0, 0, 32, 32)
    Stone = Load_Texture("./textures/stone1.png", 0, 0, 32, 32)
    Water = Load_Texture("./textures/water.png", 0, 0, 32, 32)
    Grass1 = Load_Texture("./textures/badborder.png", 32, 0, 32, 32)
    Texture_Tags = {"1" : Grass, "2": Stone, "3" : Water, "4" : Grass1}




