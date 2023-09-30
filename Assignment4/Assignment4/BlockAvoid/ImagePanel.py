import pygame
from View import View

class ImagePanel(View):
    def __init__(self):
        self.PositionX = 0
        self.PositionY = 0
    def draw(self, surface):
        self.image = pygame.image.load("StartScreen.bmp")
        surface.blit(self.image, (self.PositionX, self.PositionY))