#!/usr/bin/env python3
import pygame

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


    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    Grass = Load_Texture("/home/syliel/pygamerpg/textures/haileygrass.png", Size)
    Stone = Load_Texture("/home/syliel/pygamerpg/textures/stone1.png", Size)
    Water = Load_Texture("/home/syliel/pygamerpg/textures/water.png", Size)



    Texture_Tags = {"1" : Grass, "2": Stone, "3" : Water}
