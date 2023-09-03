#Main game loop

#Event handler 
running = True 
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 
      
  keys = pygame.key.get_pressed()

  #Horizontal player movement
  if keys[pygame.K_LEFT]:
    playerSpeedX = -PLAYER_SPEED
  elif keys[pygame.K_RIGHT]:
    playerSpeedX = PLAYER_SPEED
  else:
    playerSpeedX = 0

  #Vertical player movement
  if keys[pygame.K_SPACE] and onGround:
    playerSpeedY = jumpPower
    onGround = False

  #Gravity
  if not onGround:
    playerSpeedY += gravity 

  #Updating player positions
  player.x += playerSpeedX
  player.y += playerSpeedY

  #Keep sprite in the game window
  if player.left < 0:
    player.left = 0 
  if player.right > SCREEN_WIDTH:
    player.right = SCREEN_WIDTH
  if player.top < 0:
    player.top = 0 
  if player.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
    player.bottom = SCREEN_HEIGHT - GROUND_HEIGHT
    onGround = True 

  #Clearing the screen
  screen.fill(WHITE)

  #Drawing the ground
  pygme.draw.rect(screen, (0, 255, 0), (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT)

  #Drawing the sprite 
  pygame.draw.rect(screen, (0, 255, 0), player)

  #pygame.display.update()



