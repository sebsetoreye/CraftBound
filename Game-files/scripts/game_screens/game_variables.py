import pygame


#### Screen ####
# Constants
ROWS = 15
COLS = 40
CELL_SIZE = 20
MARGIN_ROWS = 2  # Number of reserved rows at the top and bottom
walls = []

new_WINDOW_WIDTH = 800
new_WINDOW_HEIGHT = 400



# Colors
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
AGENT_COLOR = (255, 0, 0)
BUTTON_COLOR = (100, 100, 100)
BUTTON_CLICK_COLOR = (150, 150, 150)
BUTTON_TEXT_COLOR = (255, 255, 255)

Wall_Color = ( 255, 255, 255)


# Button dimensions
BUTTON_SIZE = 30

BUTTON_WIDTH = 200 #Start screen
BUTTON_HEIGHT = 50 #Start screen



# Setup on clock
clock = pygame.time.Clock()
