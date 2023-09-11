# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if play_button.is_clicked(pos):
                print("Play button clicked!")
                # Add code here to start the game
            elif quit_button.is_clicked(pos):
                pygame.quit()
                sys.exit()


