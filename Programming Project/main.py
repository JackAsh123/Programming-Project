#import necessary modules
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60 

#screen dimensions
screen_width = 1000
screen_height = 1000

#define and name the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jario')

#define game variables
tile_size = 50


#load images
moon_img = pygame.image.load('Assets/pixel_moon.png')
bg_img = pygame.image.load('Assets/cave_city_background.png')
scale_bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
#temporary drawn grid so I can see what blocks to change to what platforms
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class PlayerSprite():  #instantiating the players sprite and scaling it to fit the map
	def __init__(self, x, y): #constructor method
		self.images_right = [] 
		self.indef=x = 0
		self.counter = 0
		for num in range(1, 5):
			img = pygame.image.load("Assets/elven_man{num}.png")
		self.image = pygame.transform.scale(img, (30, 60))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vel_y = 0
		self.jumped = False

	def update(self):
		dx = 0
		dy = 0


		#get key presses 
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False:
			self.vel_y = -15
			self.jumped = True

		if key[pygame.K_SPACE] == False:
			self.jumped = False

		if key[pygame.K_LEFT]:
			dx -= 5

		if key[pygame.K_RIGHT]:
			dx += 5


		#adding gravity 
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10 #sets terminal velocity to ten so it can't be surpassed
		dy += self.vel_y

		#check for collision - code this at a later stage 

		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height


		#draw the player's sprite onto the screen
		screen.blit(self.image, self.rect)

class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		stone_img = pygame.image.load('Assets/stone_block1.png') #assigns variable name to img from Assets folder 
		moss_img = pygame.image.load('Assets/stone_block2.jpg')

		row_count = 0 #allows to put block images into specific tiles at the right scale
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(stone_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(moss_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1]) #blits tiles onto the screen



world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



player_sprite = PlayerSprite(100, screen_height - 110)
world = World(world_data)

run = True
while run:

	clock.tick(fps)

	screen.blit(scale_bg_img, (0, 0))
	screen.blit(moon_img, (100, 100))

	world.draw()
	player_sprite.update()

	draw_grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
	pygame.display.update()

pygame.quit()
