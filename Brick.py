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
	if self.ID == 'g':
            img = pygame.image.load('Assets/grass.bmp')
        
	elif self.ID == 'b':
            img = pygame.image.load('Assets/brick.bmp')

        elif self.ID == 's':
            img = pygame.image.load('Assets/stone.bmp')
        
        elif self.ID == 'q':
            img = pygame.image.load('Assets/qmark.bmp')
	window.blit(img, (self.x, self.y))
