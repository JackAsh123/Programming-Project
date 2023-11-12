#Main game loop
import pygame
from pygame.locals import *

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jario")


  keys = pygame.key.get_pressed()

  #Horizontal sprite movement
  if keys[pygame.K_LEFT]:
    spriteSpeedX = -SPRITE_SPEED
  elif keys[pygame.K_RIGHT]:
    spriteSpeedX = SPRITE_SPEED
  else:
    spriteSpeedX = 0

  #Vertical sprite movement
  if keys[pygame.K_SPACE] and onGround:
    spriteSpeedY = jumpPower
    onGround = False

  #Gravity
  if not onGround:
    spriteSpeedY += gravity 

  #Updating sprite positions
  sprite.x += spriteSpeedX
  sprite.y += spriteSpeedY

  #Keep sprite in the game window
  if sprite.left < 0:
    sprite.left = 0 
  if sprite.right > SCREEN_WIDTH:
    sprite.right = SCREEN_WIDTH
  if sprite.top < 0:
    sprite.top = 0 
  if sprite.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
    sprite.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
    onGround = True 

  #Clearing the screen
  screen.fill(WHITE)

  #Drawing the ground
  pygme.draw.rect(screen, (0, 255, 0), (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)

  #Drawing the sprite 
  pygame.draw.rect(screen, (0, 255, 0), sprite)

  #pygame.display.update()



