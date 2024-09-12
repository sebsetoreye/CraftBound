import pygame
import sys
from .start_screen_variables import *


def draw_start_screen():
    screen.fill(BACKGROUND_COLOR)
    
    # Render text
    title_text = font.render('CraftBound', True, WHITE)
    instruction_text = small_font.render('Press Enter to Start', True, WHITE)
    
    # Position text
    title_rect = title_text.get_rect(center=(Start_WINDOW_WIDTH/2, Start_WINDOW_HEIGHT/2 - 50))
    instruction_rect = instruction_text.get_rect(center=(Start_WINDOW_WIDTH/2, Start_WINDOW_HEIGHT/2 + 50))
    
    # Draw text on the screen
    screen.blit(title_text, title_rect)
    screen.blit(instruction_text, instruction_rect)
    
    pygame.display.flip()

