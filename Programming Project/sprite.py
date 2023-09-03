#Sprite setup

#Sprite dimensions
sprite = pygame.Rect(50, SCREEN_HEIGHT - GROUND_HEIGHT - SPRITE_HEIGHT, SPRITE_WIDTH, SPRITE_HEIGHT)

#Sprite Characteristics 
spriteSpeedX = 0
spriteSpeedY = 0
gravity = 0.5
jumpPower  = -10
onGround = False 
