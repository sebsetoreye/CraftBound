import pygame
from scripts.game_screens.game_variables import *
from scripts.gui_screens.start_screen_files.start_screen_variables import *
from scripts.game_screens.game_functions import *
from scripts.Global.global_variables import *
import random

def draw_enemy(x, y):
    # Clear the enemy list before appending the current position
    enemy.clear()
    rect = pygame.Rect(y * CELL_SIZE, (x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, AGENT_COLOR, rect)
    enemy.append((x, y))  # Append the current position of the enemy



# Function to move enemy towards player
def move_enemy_towards_player(enemy_x, enemy_y, player_x, player_y):
    if enemy_x < player_x:
        new_enemy_x = enemy_x + 1
    elif enemy_x > player_x:
        new_enemy_x = enemy_x - 1
    else:
        new_enemy_x = enemy_x

    if enemy_y < player_y:
        new_enemy_y = enemy_y + 1
    elif enemy_y > player_y:
        new_enemy_y = enemy_y - 1
    else:
        new_enemy_y = enemy_y

    # Check for collision before moving
    if not is_enemy_collision(new_enemy_x, new_enemy_y):
        return new_enemy_x, new_enemy_y
    
    elif is_enemy_collision(new_enemy_x, new_enemy_y):
        print("hit")

    return enemy_x, enemy_y  # Return original position if collision


def is_enemy_collision(x, y):
    return (x, y) in enemy