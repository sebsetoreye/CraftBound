
import pygame
import sys

from .game_variables import *
from scripts.gui_screens.start_screen_variables import *





def change_screen_size():
    global screen
    screen = pygame.display.set_mode((new_WINDOW_WIDTH, new_WINDOW_HEIGHT))


# Function to draw the grid
# // Need to change
def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    for x in range(0, new_WINDOW_WIDTH, CELL_SIZE):
        for y in range(MARGIN_ROWS * CELL_SIZE, (ROWS + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

# Function to draw the agent/player
def draw_agent(x, y):
    rect = pygame.Rect(y * CELL_SIZE, (x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, AGENT_COLOR, rect)

# Function to get grid coordinates from mouse position
def get_grid_position(mouse_pos):
    mouse_x, mouse_y = mouse_pos
    grid_x = (mouse_y // CELL_SIZE) - MARGIN_ROWS
    grid_y = mouse_x // CELL_SIZE
    if 0 <= grid_x < ROWS and 0 <= grid_y < COLS:
        return grid_x, grid_y
    return None

# Function to draw buttons
#// Need to change 
def draw_button(text, x, y, size, is_clicked):
    color = BUTTON_CLICK_COLOR if is_clicked else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, size, size))
    font = pygame.font.SysFont(None, 24)
    text_render = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_render.get_rect(center=(x + size // 2, y + size // 2))
    screen.blit(text_render, text_rect)
