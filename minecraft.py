import pygame, sys, random
from pygame.locals import *

DIRT=0
GRASS=1
WATER=2
COAL=3
ROCK=4
LAVA=5
DIAMOND=6
EMERALD=7
CLOUD=8


WHITE = (255,255,255)
BLACK = (0,0,0)

cloudx = -200
cloudy = 0

textures = {
		GRASS:pygame.image.load('pygame-textures/grass.png'),
		DIRT:pygame.image.load('pygame-textures/dirt.png'),
		WATER:pygame.image.load('pygame-textures/water.png'),
		COAL:pygame.image.load('pygame-textures/coalore.png'),
		ROCK:pygame.image.load('pygame-textures/rock.png'),
		LAVA:pygame.image.load('pygame-textures/lava.png'),
		DIAMOND:pygame.image.load('pygame-textures/diamondore.png'),
		EMERALD:pygame.image.load('pygame-textures/emeraldore.png'),
		CLOUD:pygame.image.load('pygame-textures/cloud.png')
		    }

inventory = {
			DIRT:0,
			GRASS:0,
			COAL:0,
			ROCK:0,
			DIAMOND:0,
			EMERALD:0
			}

TILESIZE=40
MAPWIDTH=30
MAPHEIGHT=20

PLAYER = pygame.image.load('pygame-textures/player.png')
playerPos = [0,0]

resources = [DIRT, GRASS, ROCK, COAL, DIAMOND, EMERALD]
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

pygame.init()
DISPLAYSURF=pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))
INVFONT = pygame.font.Font("OpenSans-Light.ttf", 18)
for rw in range(MAPHEIGHT):
	for cl in range(MAPWIDTH):
		randomNumber = random.randint(0,500)
		if randomNumber >=1 and randomNumber <=150:
			tile = DIRT
		elif randomNumber >=151 and randomNumber <=250:
			tile = WATER
		elif randomNumber >=251 and randomNumber <=281:
			tile = COAL
		elif randomNumber >=282 and randomNumber <=352:
			tile = ROCK
		elif randomNumber >=353 and randomNumber <=370:
			tile = LAVA
		elif randomNumber ==371:
			tile = DIAMOND
		elif randomNumber ==372:
			tile = EMERALD
		else:
			tile = GRASS
		tilemap[rw][cl] = tile
pygame.display.set_caption('Minecraft Python Edition v0.2')
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				playerPos[0] += 1
			if (event.key == K_LEFT) and playerPos[0] > 0:
				playerPos[0] -= 1
			if (event.key == K_UP) and playerPos[1] > 0:
				playerPos[1] -= 1
			if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT -1:
				playerPos[1] += 1
			if (event.key == K_SPACE):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile] += 1
				tilemap[playerPos[1]][playerPos[0]] = DIRT
				print(inventory)
			if (event.key == K_1):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIRT] > 0:
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]]=DIRT
					inventory[currentTile] += 1
			if (event.key == K_2):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[GRASS] > 0:
					inventory[GRASS] -= 1
					tilemap[playerPos[1]][playerPos[0]]=GRASS
					inventory[currentTile] += 1
			if (event.key == K_3):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[ROCK] > 0:
					inventory[ROCK] -= 1
					tilemap[playerPos[1]][playerPos[0]]=ROCK
					inventory[currentTile] += 1
			if (event.key == K_4):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[COAL] > 0:
					inventory[COAL] -= 1
					tilemap[playerPos[1]][playerPos[0]]=COAL
					inventory[currentTile] += 1
			if (event.key == K_5):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIAMOND] > 0:
					inventory[DIAMOND] -= 1
					tilemap[playerPos[1]][playerPos[0]]=DIAMOND
					inventory[currentTile] += 1
			if (event.key == K_6):
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[EMERALD] > 0:
					inventory[EMERALD] -= 1
					tilemap[playerPos[1]][playerPos[0]]=EMERALD
					inventory[currentTile] += 1

	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))

	cloudx+=1

	if cloudx > MAPWIDTH*TILESIZE:
		cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
		cloudx = -200

	fpsClock = pygame.time.Clock()

	placePosition = 10
	for item in resources:
		DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		textObj = INVFONT.render(str(inventory.get(item)), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition, MAPHEIGHT*TILESIZE+20))
		placePosition += 50





	pygame.display.update()
	fpsClock.tick(24)
