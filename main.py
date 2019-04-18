import pygame
from pygame.locals import *

#Tyler Matthews
#4/18/19

#Global Variables
(WIDTH, HEIGHT) = (480, 480)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
xArr = []
oArr = []
lastIndex = ''

#main function
def main():
	drawBool = False
	drawOBool = False
	(posX , posY) = (0, 0)
	pygame.init()      # Prepare the pygame module for use
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:  # Window close button clicked?
				break
			elif event.type == pygame.MOUSEBUTTONUP:
				(posX, posY) = pygame.mouse.get_pos()
				index = calculatePos(posX, posY)

				if(not(index in oArr) and not (index in xArr)): #Square not already played
					lastIndex = index #keep track of last placed value for backtracking
					if(drawOBool): #O's turn
						oArr.append(calculatePos(posX, posY))
						drawOBool = False
					else: #X's turn
						xArr.append(calculatePos(posX, posY))
						drawOBool = True
				elif(index == lastIndex): #remove last move
					lastIndex = ''
					if(drawOBool):
						xArr.remove(index)
						drawOBool = False
					else:
						oArr.remove(index)
						drawOBool = True

		draw(screen, posX, posY, drawBool, drawOBool)
	pygame.quit()     # Once we leave the loop, close the window.


#draws everything on the screen
def draw(screen, posX, posY, drawBool, drawOBool):
	screen.fill(BLACK) #Background

	for O in oArr:
		drawO(screen, O);

	for X in xArr:
		drawX(screen, X);

	drawBoard(screen)
	pygame.display.flip()

#Calculates index based on (x, y) position
def calculatePos(posX, posY):
	if(posX < (WIDTH/3)): #Left Column
		if(posY < (HEIGHT/3)):
			return 0
		elif(posY < (2*HEIGHT/3)):
			return 3
		else:
			return 6
	elif(posX < (2*WIDTH/3)): #Middle Column
		if(posY < (HEIGHT/3)):
			return 1
		elif(posY < (2*HEIGHT/3)):
			return 4
		else:
			return 7
	else: #Right Column
		if(posY < (HEIGHT/3)):
			return 2
		elif(posY < (2*HEIGHT/3)):
			return 5
		else:
			return 8

#draws 'O' at given index
def drawO(screen, index):
	pygame.draw.circle(screen, WHITE, (index%3 * int(WIDTH/3) + (int)(WIDTH/6), int(index/3) * int(HEIGHT/3) + (int)(HEIGHT/6)), int(WIDTH/6) - 5, 0)

#draws 'X' at given index
def drawX(screen, index): #index is a number 0-9)
	(x, y) = (index%3 * WIDTH/3, int(index/3) * HEIGHT/3)
	pygame.draw.lines(screen, WHITE, False, [(x, y), (x + (WIDTH/3), y + (HEIGHT/3))], 5)
	pygame.draw.lines(screen, WHITE, False, [(x, y + (HEIGHT/3)), (x + (WIDTH/3), y)], 5)

def drawBoard(screen):
	pygame.draw.lines(screen, RED, False, [(WIDTH/3, 0), (WIDTH/3, HEIGHT)], 10)
	pygame.draw.lines(screen, RED, False, [(2*WIDTH/3, 0), (2*WIDTH/3, HEIGHT)], 10)
	pygame.draw.lines(screen, RED, False, [(0, HEIGHT/3), (WIDTH, HEIGHT/3)], 10)
	pygame.draw.lines(screen, RED, False, [(0, 2*HEIGHT/3), (WIDTH, 2*HEIGHT/3)], 10)


#Call main function
main()
