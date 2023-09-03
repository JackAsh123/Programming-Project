#Player setup

#Player dimensions
player = pygame.Rect(50, SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

#Player Characteristics 
playerSpeedX = 0
playerSpeedY = 0
gravity = 0.5
jumpPower  = -10
onGround = False 
