import pygame
from globals import Globals
from GameState import GameState
import pygame
from ViewManager import ViewManager
from ModelManager import ModelManager
from ControllerManager import ControllerManager
from ImagePanel import ImagePanel
class SplashScreen(ModelManager,ViewManager,ControllerManager):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.background = pygame.Color(128,128,0)
        self.ScreenImage = ImagePanel()
    def draw(self,surface):
        surface.fill(self.background)
        super().draw(surface)
        self.ScreenImage.draw(surface) 
        pygame.display.flip()
    def update(self):
        pass
    def handleEvent(self,event):
        if (event.type == pygame.QUIT):
            Globals.done = True
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                Globals.currentState = GameState.GAMEPLAY
                
        



