import pygame
import random

class IntroGrass:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    
    def update(self):
        self.x -= 10

    def render(self,window):
        img = pygame.image.load('Assets/Images/grass.bmp')
        window.blit(img,(self.x,self.y))
