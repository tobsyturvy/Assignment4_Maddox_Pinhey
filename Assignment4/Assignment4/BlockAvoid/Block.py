import pygame
from Model import Model
from View import View
RED = (255,0,0)

class Block(Model,View):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = 0
        pygame.draw.rect(self.image,RED,[self.rect.x,self.rect.y,32,32])

    def update(self):
        newx = self.rect.x + self.dx
        newy = self.rect.y + self.dy
        # bounce
        if newx < 0 or newx > 768:
            self.dx = -self.dx
            newx += self.dx
        if newy < 0 or newy > 568:
            self.dy = -self.dy
            newy += self.dy
        self.rect.x = newx
        self.rect.y = newy

    def draw(self,surface):
        surface.blit(self.image,self.rect)