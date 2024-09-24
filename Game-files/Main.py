import sys
import pygame
from scripts.game_screens.Game import main as game_main
from scripts.gui_screens.start_screen import draw_start_screen, Start_WINDOW_HEIGHT, Start_WINDOW_WIDTH

# Initialize Pygame
pygame.init()

# Set the screen dimensions and create the display
screen = pygame.display.set_mode((Start_WINDOW_WIDTH, Start_WINDOW_HEIGHT))  # Create the screen for the start

# Running the game
while True:
    draw_start_screen()  # Draw the start screen

    # Event handling for the start screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Start the game when Enter is pressed
                game_main()  # Call the main game function

    pygame.time.delay(100)  # Control the frame rate
