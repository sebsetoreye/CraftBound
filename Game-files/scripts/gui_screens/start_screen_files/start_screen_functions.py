import pygame
import sys
from .start_screen_variables import *

# Load the background image at the beginning of your main function or a setup function
start_background_image = pygame.image.load('Game-files/sprites/logo.jpeg')
start_background_image = pygame.transform.scale(start_background_image, (Start_WINDOW_WIDTH, Start_WINDOW_HEIGHT))  # Scale it to fit the start window

def draw_start_screen():
    # Draw the background image
    screen.blit(start_background_image, (0, 0))  # Draw the image at the top-left corner
    
    # Render text
    instruction_text = small_font.render('Press Enter to Start', True, WHITE)
    
    # Position title text
    instruction_rect = instruction_text.get_rect(center=(Start_WINDOW_WIDTH / 2, Start_WINDOW_HEIGHT / 2 + 130))
    
    # Draw text on the screen
    screen.blit(instruction_text, instruction_rect)
    
    pygame.display.flip()
