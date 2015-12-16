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

background = pygame.image.load("Assets/background.bmp")

screenWidth = 800
screenHeight = 640
fps = 60

gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("FlipOut!")

player = Player(400,300)
randcirclelist = []

score = 0
count = 0
lives = 3

class message:
	## VARIOUS FONTS STYLES
	small_font =  pygame.font.Font('Fonts/tlpsmb.ttf',25)
	med_font =  pygame.font.Font('Fonts/PAC-FONT.TTF',40)
	large_font =  pygame.font.Font('Fonts/PAC-FONT.TTF',60)
	def_font =  pygame.font.Font('Fonts/classic.TTF',25)
	gameov_font  = pygame.font.Font('Fonts/eddie.ttf',50)
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
	def setup(self,(width,height),(posx,posy)):
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
	def display_score(self,msg,posx,posy):
		screen_text = message.def_font.render(msg,True,white)	
		gameDisplay.blit(screen_text,[posx,posy])

	## DISPLAYING  THE TEXT OBJECT
	def message_to_screen(self,msg,color,y_displace=0,size="small",text="start",intro="True"):
		if(text=="start"):				
			if(self.setup((80,19),(screenWidth/2,screenHeight/2+y_displace))):
				gamem();
			if(self.hover((80,19),(screenWidth/2,screenHeight/2+y_displace)))	:			
				color = yellow
		elif(text=="exit"):				
			if(self.setup((80,19),(screenWidth/2,screenHeight/2+y_displace))):
				intro = False
			if(self.hover((80,19),(screenWidth/2,screenHeight/2+y_displace)))	:			
				color = yellow
			
		textSurf , textRect = self.text_objects(msg,color,size)
		textRect.center = (screenWidth/2),(screenHeight/2)+y_displace
		gameDisplay.blit(textSurf,textRect)
		
		return intro
def GameOver():
		gameExit = False
		game = message()
		gameOver = True	
		while gameOver:
			gameOver=game.message_to_screen("Game over",red,y_displace=-50,size="medium")
			gameOver=game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="small")
			
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#gameOver = True
					gameExit = True	
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameExit = True
						#gameOver = True
						game_intr()
					elif event.key == pygame.K_c:
						gameExit = False
						gameOver = False
						gamem()	
def game_intr():
	game = message()
	intro = True 
  	pygame.mixer.music.stop()
	pygame.mixer.music.load('Assets/Sounds/introMusic.mp3')
	pygame.mixer.music.play(-1)
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
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro = False
					pygame.quit()
					quit()
					
			pygame.display.update()

lives = 3
def gamem():

  	pygame.mixer.music.stop()
	pygame.mixer.music.load('Assets/Sounds/gameMusic.mp3')
	pygame.mixer.music.play(-1)
	img = pygame.image.load('Assets/creeper.bmp')
	global lives
	levelobj = Level(0)
	brickList = []
	level = levelobj.level_design()
	for y in range(len(level)):
		for x in range(len(level[y])):
			if (level[y][x] == 1):
				brickList.append(Brick(x*32,y*32,(205,155,100)))
			
	for brick in brickList:
		brick.render(gameDisplay)
        game = message()
    	score = 0
	count = 1
	lead_x_change = 0
	block_size = 32
	gameOver = False
	gameExit = False
	while not gameExit:
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
				elif event.key == pygame.K_SPACE:
					player.flip()
					img = pygame.transform.rotate(img,180)			
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
					
		if lead_x_change >= 0:
	        	player.x += lead_x_change/4 - lead_x_change/5
    		else:
        		player.x += -lead_x_change/4 + lead_x_change/5
					
                count += lead_x_change/5
		gameDisplay.fill(white)
		gameDisplay.blit(background, (0,0))
		gameOver,img = player.update(brickList,gameOver,img)
		if (gameOver):
			lives -= 1
			gamem()
		player.render(gameDisplay,img)		
        	if (int(count)%50==0):
            		score+=1	
		for brick in brickList:
			brick.x -= lead_x_change
			brick.render(gameDisplay)
		pygame.draw.rect(gameDisplay, black, (0,0,800,32))
		game.display_score("Score   "+str(score),0,0)
		game.display_score("Lives   "+str(lives),690,0)	
		if lives == 0:
			GameOver()
		pygame.display.update()			
		clock.tick(fps)

game_intr()
pygame.quit()
quit()					

