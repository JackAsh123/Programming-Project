import pygame
import sys

#initialise pygame
pygame.init()

#Event handler 
running = True 
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 

#Creating game window 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jario")

#Blit the screen
screen.blit()
pygame.display.flip()








