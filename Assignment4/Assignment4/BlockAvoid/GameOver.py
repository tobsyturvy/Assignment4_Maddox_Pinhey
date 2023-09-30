import pygame
from globals import Globals
from GameState import GameState
from ViewManager import ViewManager
from ModelManager import ModelManager
from ControllerManager import ControllerManager
class GameOver(ModelManager,ViewManager,ControllerManager):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.background = pygame.Color(255,0,50)
    def draw(self,surface):
        surface.fill(self.background)
        super().draw(surface)
        pygame.display.flip()    
    def update(self):
        pass
    def handleEvent(self,event):
        if (event.type == pygame.QUIT):
            Globals.done = True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_q):
                Globals.done = True
