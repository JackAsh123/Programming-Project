import sys
import pygame
from pygame.locals import*  #Importing all necessary modules

pygame.init()#Initialising pygame

screenWidth = 600
screenHeight = 600#Setting dimensions of the window
window = pygame.display.set_mode((screenWidth,screenHeight)) #Set the size of the screen using
#pygame.display.set_mode()

img = pygame.image.load("Assets/cave_city_background.png")#Load the image
window.blit(window, (screenWidth, screenHeight))#Blit

pygame.display.update()#Update the screen









