import pygame


#initialise
pygame.init()


# Define fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

#Start screen
Start_WINDOW_WIDTH = 1200
Start_WINDOW_HEIGHT = 600

# Colors
BACKGROUND_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

#Setup display
screen = pygame.display.set_mode((Start_WINDOW_WIDTH, Start_WINDOW_HEIGHT))
pygame.display.set_caption("CraftBound")


