#!/usr/bin/env python3
import pygame
from scripts.NPC import *
pygame.init()

class Player:
    def __init__(self, name):
        self.name = name
        self.facing = "south"
        self.health = 100
        sprite = pygame.image.load("./textures/mousie1.png")
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]

        # Get Player Faces
        self.faces = get_faces(sprite)

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)
