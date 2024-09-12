import pygame
import sys

from .start_screen_variables import *
from .start_screen_functions import *

pygame.init()


def start_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key pressed
                    return
        
        draw_start_screen()