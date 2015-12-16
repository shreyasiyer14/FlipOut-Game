import pygame

class Brick:
    def __init__(self, x, y,color,ID):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.ID = ID
	self.color = color

    def render(self, window):
        if self.ID == 2:
            img = pygame.image.load('Assets/grass.bmp')
        else:
            img = pygame.image.load('Assets/brick.bmp')
        window.blit(img, (self.x, self.y))
