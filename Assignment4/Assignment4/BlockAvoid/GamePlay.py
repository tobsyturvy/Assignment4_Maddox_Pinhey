import pygame
from globals import Globals
from GameState import GameState
from Block import Block
from Player import Player
from ModelManager import ModelManager
from ViewManager import ViewManager
from ControllerManager import ControllerManager
from ElapsedTimePanel import ElapsedTime
from TextPanel import Text
from ImagePanel import ImagePanel
from ElapsedTimePanel import ElapsedTime

import random


class ScreenChanger(ViewManager):
    startscreen = pygame.image.load("StartScreen.bmp")


class GamePlay(ModelManager,ViewManager,ControllerManager):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.background = pygame.Color(10,10,10)
        self.blocks = []
        self.player = Player()
        self.addController(self.player)
        self.addView(self.player)
        self.addModel(self.player)
        self.timeToNextBlock = 300
        self.spawnBlock(self.player.rect.x,self.player.rect.y)

    def spawnBlock(self,playerX, playerY):
        block = Block()
        self.addModel(block)
        self.addView(block)
        self.blocks.append(block)
        if playerX < 400:
            block.rect.x = random.randint(400,768)
        else:
            block.rect.x = random.randint(0,400)
        block.rect.y = random.randint(0,568)
        block.dx = random.randint(-1,1)*2
        block.dy = random.randint(-1,1)*2
    def update(self):
        #move everyone
        super().update()
        ElapsedTime.updateTime(self)
        # window specific update code
        self.timeToNextBlock -= 1
        if self.timeToNextBlock == 0:
            self.timeToNextBlock = 300
            self.spawnBlock(self.player.rect.x, self.player.rect.y)
        # check for collision
        for block in self.blocks:
            if (self.player.rect.colliderect(block.rect) == True):
                Globals.currentState = GameState.GAMEOVER
    def draw(self,surface):
        surface.fill(self.background)
        super().draw(surface)
        pygame.display.flip()
    def handleEvent(self,event):
        if (event.type == pygame.QUIT):
            Globals.done = True
        else:
            super().handleEvent(event)
            


