#Define button class
def Button:
  def __init__(self, x, y, button_width, button_height, text):
    self.rect = pygame.Rect(x, y, button_width, button_height)
    self.text = text

  def draw(self):
    pygame.draw.rect(screen, WHITE, self.rect)
    font = pygame.font.Font(None, 36)
    text =font.render(self.text, True, BLACK)
    text_Rect = text.get_rect(center = self.rect.center)
    screen.blit(text, text_Rect)

  def isClicked(self, pos):
    return self.rect.collidepoint(pos)

#Create the buttons 
play_button = Button(300, 200, 200, 50, "Play")
quit_button = Button(300, 300, 200, 50, "Quit")

screen.fill(black)
play_button.draw()
quit_button.draw()
pygame.display.update()
