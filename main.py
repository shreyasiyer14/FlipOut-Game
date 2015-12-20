import pygame
import time
import random

from Brick import *
from Player import *
from Level import *
from IntroGrass import *

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)
yellow =(255,255,0)


screenWidth = 800
screenHeight = 640
fps = 120

gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("FlipOut!")

player = Player(400,300)
randcirclelist = []

score = 0
count = 0
lives = 3
pygame.mixer.init()

creeper = pygame.image.load('Assets/creeper.bmp')
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
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
		global lives
		gameExit = True
		game = message()
		gameOver = True	
		while gameOver:
			gameOver=game.message_to_screen("Game over",red,y_displace=-50,size="medium")
			gameOver=game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="small")
			
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
						pygame.quit()
						quit()
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_c:
						gameExit = False
						gameOver = False
						lives = 3
						score = 0
						gamem()	
def game_intr():
	game = message()
	intro = True 
  	
	background = pygame.image.load("Assets/background.bmp")
	
	grass = IntroGrass(800,608)
	displace = 32
	grassList = []
	grassList.append(grass)
	pygame.mixer.music.stop()
	pygame.mixer.music.load('Assets/Sounds/introMusic.mp3')
	pygame.mixer.music.play(-1)
	count = 1
	x = 400
	y = 300

	dx = random.randrange(-10,10)
	dy = random.randrange(-10,10)

	while intro:
			if count%3==0:
				grass = IntroGrass(800,608)
				grassList.append(grass)
			gameDisplay.fill(black)
			gameDisplay.blit(background,(0,0))
			count += 1
			for grass in grassList:
				grass.update()
				if (grass.x < -32):
					grassList.remove(grass)
				grass.render(gameDisplay)
			
			if (x > 768):
				dx *= -1
			elif (x < 0):
				dx *= -1
			if (y < 0):
				dy *= -1
			elif (y > 608):	
				dy *= -1	
			x += dx
			y += dy
			pygame.draw.rect(gameDisplay, black, (x - 2, y - 2, 36, 36))
			gameDisplay.blit(creeper, (x,y))	
			intro=game.message_to_screen("FlipOut!",(135,155,105),-150,size="large",text="none")
			intro=game.message_to_screen("START GAME",(139,0,139),-20)
			intro=game.message_to_screen("EXIT GAME",(139,0,139),20,text="exit")
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro = False
					pygame.quit()
					quit()
					
			pygame.display.update()

lives = 3
sp_itms = 0
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
			if (level[y][x] != 0):
				brickList.append(Brick(x*32,y*32,(205,155,100),level[y][x]))
			
	for brick in brickList:
		brick.render(gameDisplay)
        game = message()
    	global score
	sp_itms = 0
	count = 1
	time = 60
	
	lead_x_change = 0
	block_size = 32
	gameOver = False
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = True		
				elif event.key == pygame.K_LEFT: 	
					lead_x_change = -5
				elif event.key == pygame.K_RIGHT:	
					lead_x_change = 5
				elif event.key == pygame.K_SPACE:
					player.flip()
	        	        	points_sound = pygame.mixer.Sound("beep.wav")
        	        	    	points_sound.play()
					img = pygame.transform.rotate(img,180)
							
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
					
		if lead_x_change >= 0:
	        	player.x += lead_x_change/4 - lead_x_change/5
			time -= 0.05
    		else:
        		player.x += -lead_x_change/4 + lead_x_change/5
					
                count += lead_x_change/5
		gameDisplay.fill(white)

		if (score - 5 >= 0 and score + 5 <= 15):
			background = pygame.image.load("Assets/background.bmp")
		else:
			background = pygame.image.load("Assets/background.bmp")
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
			if (brick.ID == 'q' and detectCollisions(player.x,player.y,player.width,player.height,brick.x,brick.y,32,32)):
				brickList.remove(brick)
				sp_itms += 1
				player.flip()
			brick.render(gameDisplay)
		pygame.draw.rect(gameDisplay, black, (0,0,800,32))
		game.display_score("Score   "+str(score),0,0)
		game.display_score("Items  "+str(sp_itms),250,0)
		game.display_score("Lives   "+str(lives),690,0)	
		game.display_score("Time   "+str(int(time)),420,0)
		if lives == 0 or time == 0:
			GameOver()
		pygame.display.update()			
		clock.tick(fps)

game_intr()
pygame.quit()
quit()					

