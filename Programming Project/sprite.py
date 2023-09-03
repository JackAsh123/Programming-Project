#Sprite setup

#Sprite dimensions
player = pygame.Rect(50, SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

#Sprite Characteristics 
spriteSpeedX = 0
spriteSpeedY = 0
gravity = 0.5
jumpPower  = -10
onGround = False 
