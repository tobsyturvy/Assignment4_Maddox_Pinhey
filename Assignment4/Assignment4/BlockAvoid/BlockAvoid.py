import pygame, os, sys
from pygame import key
from pygame.locals import *
from globals import Globals
from Block import Block
from Player import Player
import random
from SplashScreen import SplashScreen
from GamePlay import GamePlay
from GameOver import GameOver
from GameState import GameState
from ElapsedTimePanel import ElapsedTime

states = {}
states[GameState.SPLASHSCREEN] = SplashScreen()
states[GameState.GAMEOVER] = GameOver()
states[GameState.GAMEPLAY] = GamePlay()

Globals.currentState = GameState.SPLASHSCREEN


pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
Globals.done = False

def main():
    global states
    global screen
    
    while (Globals.done == False):
        for event in pygame.event.get():
            states[Globals.currentState].handleEvent(event)
        states[Globals.currentState].update()
        states[Globals.currentState].draw(screen)
        fpsClock.tick(60)

main()

