#Set HUD font
font = pygame.font.Font(None, 36)

#set the initial score and lives tally
score = 0
lives = 3

#Function to update the score
def updateScore(points):
  global score
  score += points

#Function to update the lives
def updateLives(life):
  global lives
  lives += life

#Render the score
scoreText = font.render("Score: " + str(score), True, (255, 255, 255))
screen.blit(text, (10,10))

#Render the lives
livesText = font.render("Lives: ", + str(lives), True, (255,255,255))
screen.blit(text, (50,10))

#Update display
pygame.display.flip()

#Control frame rate
clock.tick(60)

#Quit pygame
pygame.quit()


