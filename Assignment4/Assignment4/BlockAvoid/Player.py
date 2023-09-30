import pygame
from Model import Model
from View import View
from Controller import Controller
GREEN = (0,255,0)
class Player(Model,View,Controller):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([32,32])
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = 0
        self.rect.x = 400
        self.rect.y = 300
        pygame.draw.rect(self.image,GREEN,[0,0,32,32])

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

    def handleEvent(self,event):
        if (event.type == pygame.KEYDOWN):
            self.dx = 0
            self.dy = 0
            if (event.key == pygame.K_UP):
                self.dy = -5
            elif (event.key == pygame.K_DOWN):
                self.dy = 5
            elif (event.key == pygame.K_LEFT):
                self.dx = -5
            elif (event.key == pygame.K_RIGHT):
                self.dx = 5

