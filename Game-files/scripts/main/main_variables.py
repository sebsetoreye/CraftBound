import pygame


#### Screen ####
# Constants
ROWS = 10
COLS = 30
CELL_SIZE = 20
MARGIN_ROWS = 2  # Number of reserved rows at the top and bottom
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = (ROWS + 2 * MARGIN_ROWS) * CELL_SIZE  # Adjusted for margins

#Start screen
Start_WINDOW_WIDTH = 8000
Start_WINDOW_HEIGHT = 600

# Colors
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
AGENT_COLOR = (255, 0, 0)
BUTTON_COLOR = (100, 100, 100)
BUTTON_CLICK_COLOR = (150, 150, 150)
BUTTON_TEXT_COLOR = (255, 255, 255)



# Button dimensions
BUTTON_SIZE = 30

BUTTON_WIDTH = 200 #Start screen
BUTTON_HEIGHT = 50 #Start screen

# Setup the display
screen_a = pygame.display.set_mode((Start_WINDOW_WIDTH, Start_WINDOW_HEIGHT))
pygame.display.set_caption("CraftBound")


screen_b = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CraftBound")



# Setup on clock
clock = pygame.time.Clock()


#changing veriable
screen_start = screen_a
screen = screen_b