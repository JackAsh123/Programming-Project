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
