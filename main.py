import pygame
import time
import random

from Brick import *
from Player import *
from Level import *
from IntroCircle import *

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)
yellow =(255,255,0)

background = pygame.image.load("Assets/bck.png")

screenWidth = 800
screenHeight = 640
fps = 60

pygame.mixer.music.load('Assets/Sounds/Music.mp3')
gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))

levelobj = Level(0)
brickList = []
level = levelobj.level_design()

player = Player(400,300)
randcirclelist = []

for y in range(len(level)):
	for x in range(len(level[y])):
		if (level[y][x] == 1):
			brickList.append(Brick(x*32,y*32,(205,155,100)))
			
for brick in brickList:
	brick.render(gameDisplay)

class message:
	## VARIOUS FONTS STYLES
	small_font =  pygame.font.Font('Fonts/tlpsmb.ttf',25)
	med_font =  pygame.font.Font('Fonts/PAC-FONT.TTF',40)
	large_font =  pygame.font.Font('Fonts/PAC-FONT.TTF',60)
	
	def __init__(self):
		pass
	## MAKING TEXT MSG ENTERED TO AN OBJECT
	def text_objects(self,text,color,size="small"):
		if size =="small":
			textSurface = message.small_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
		elif size =="medium":
			textSurface = message.med_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
		elif size =="large":
			textSurface = message.large_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
	## 	
	def set(self,(width,height),(posx,posy)):
		posx1,posy1 = pygame.mouse.get_pos()
		if(posx1>=posx-width and posx1<=(posx +width)) and (posy1>=posy and posy1<=(posy + height)):	
			if(pygame.mouse.get_pressed()[0]):
				return True
		return False
	def hover(self,(width,height),(posx,posy)):
		posx1,posy1 = pygame.mouse.get_pos()
		if(posx1>=posx-width and posx1<=(posx +width)) and (posy1>=posy-height and posy1<=(posy + height)):	
			return True
		return False

	## DISPLAYING SCORE	
	def display_score(self,msg):
		screen_text = message.med_font.render(msg,True,black)	
		gameDisplay.blit(screen_text,[0,0])

	## DISPLAYING  THE TEXT OBJECT
	def message_to_screen(self,msg,color,y_displace=0,size="small",text="start",intro="True"):
		
			
		if(text=="start"):				
			if(self.set((50,17),(screenWidth/2,screenHeight/2+y_displace))):
				gamem();
			if(self.hover((50,17),(screenWidth/2,screenHeight/2+y_displace)))	:			
				color = yellow
		elif(text=="exit"):				
			if(self.set((50,17),(screenWidth/2,screenHeight/2+y_displace))):
				intro = False
			if(self.hover((50,17),(screenWidth/2,screenHeight/2+y_displace)))	:			
				color = yellow
			
		textSurf , textRect = self.text_objects(msg,color,size)
		textRect.center = (screenWidth/2),(screenHeight/2)+y_displace
		gameDisplay.blit(textSurf,textRect)
		
		return intro
		
def game_intr():
	game = message()
	intro = True 
	while intro:
			gameDisplay.fill(black)
			circle = IntroCircle(5)
			randcirclelist.append(circle)
            		for circle in randcirclelist:
               			circle.update()
                		if circle.radius >= 500:
                    			randcirclelist.remove(circle)
                		circle.render(gameDisplay)
			intro=game.message_to_screen("FlipOut!",(155,155,105),-150,size="large",text="none")
			intro=game.message_to_screen("START GAME",white,-20)
			intro=game.message_to_screen("EXIT GAME",white,20,text="exit")
			pygame.display.update()
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 0
					
				

def gamem():
    	pygame.mixer.music.play(-1)
	lead_x_change = 0
	#lead_y_change = 0
	block_size = 32
	gameOver = False
	gameExit = False
	while not gameExit:
		## OUTER LOOP FOR GAME  	
		while gameOver == True :
			## INNER LOOP FOR GAME OVER
			gameDisplay.fill(white)
			gameOver=game.message_to_screen("Game over",red,y_displace=-50,size="large")
			gameOver=game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="medium")
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver =False
					gameExit = True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameOver =False
						gameExit = True
					elif event.key == pygame.K_c:
						gameOver =False
						gameExit = True
						game_intr()	
			
		## READING OF THE USER INPUT THROUGH KEYBOARD

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = True		
				elif event.key == pygame.K_LEFT: 	
					lead_x_change = -5
				elif event.key == pygame.K_RIGHT:	
					lead_x_change = 5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
					
		if lead_x_change >= 0:
	        	player.x += lead_x_change/4 - lead_x_change/5
    		else:
        		player.x += -lead_x_change/4 + lead_x_change/5
					
		gameDisplay.fill(white)
		gameDisplay.blit(background, (0,0))
		
		player.update(brickList)
		player.render(gameDisplay)
		
		for brick in brickList:
			brick.x -= lead_x_change
			brick.render(gameDisplay)	
		pygame.display.update()			
		clock.tick(fps)

game_intr()
pygame.quit()
quit()					
