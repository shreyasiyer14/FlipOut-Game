import pygame
import random

class IntroCircle:
    def __init__ (self,r):
        self.radius = r
        self.color = (random.randrange(50,200),random.randrange(50,200),random.randrange(50,200))
        
    def update(self):
        self.radius += 5

    def render(self,window):
        pygame.draw.circle(window,self.color,(400,300),self.radius,1)
