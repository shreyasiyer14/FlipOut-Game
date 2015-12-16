import pygame

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 32
        self.width = 32
        self.velocity=0
        self.falling = True
        self.onGround = False
        self.velocity = 0
        self.direction = 1
       
    def flip(self):
        self.velocity = -10
        self.direction*=-1
        self.y += self.direction*self.velocity
        
    def detectCollisions(self, x1,y1,w1,h1,x2,y2,w2,h2):  
        if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
            return True
        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
            return True               
        elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
            return True
        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
            return True      
        else:
            return False
                    
    def update(self, blockList,gameOver): 
        hasCollided = False      
        blockX,blockY=0,0       
        for block in blockList:
            hasCollided = self.detectCollisions(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)
            if (hasCollided and (block.y == 0 or block.y == 608)):
                blockX = block.x
                blockY = block.y
                hasCollided = True
                break
	    if (hasCollided and block.y > 0 and block.y < 608):
            	gameOver = True
	    else:
                hasCollided = False
                
        if (hasCollided):
            if (self.falling == True):
		if (self.y > blockY):
			self.y = blockY + self.height
		else:
                	self.y = blockY - self.height
                self.falling = True
                self.onGround = True
                self.velocity = -10
        else:
            self.falling = True
            self.onGround = False

        if (self.onGround == False):
           self.velocity+=-0.3
	   self.falling = True
        else:
           self.direction*=-1
           self.velocity+=-0.5
           self.falling = True
           self.onGround = False
        self.y-=(self.velocity*self.direction)
       
        return gameOver 
    def render(self,window):
	img = pygame.image.load('Assets/creeper.bmp')
        pygame.draw.rect(window, (0,0,0),(self.x-2, self.y-2, self.width+4, self.height+4))
	window.blit(img,(self.x,self.y))
        

