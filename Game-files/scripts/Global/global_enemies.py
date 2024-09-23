import pygame
from scripts.game_screens.game_variables import *
from scripts.gui_screens.start_screen_files.start_screen_variables import *
from scripts.game_screens.game_functions import *
from scripts.Global.global_variables import *
from scripts.Global.global_player import Player
import random

# Enemy class to manage position and health
class Enemy:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
    
    # Method to check if the enemy is alive
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    

# Function to draw all enemies
def draw_enemy(enemies):
    # Iterate over a copy of the enemies list to avoid modifying the list while iterating
    for enemy in enemies[:]:
        if enemy.is_alive():
            # Draw the enemy if alive
            rect = pygame.Rect(enemy.y * CELL_SIZE, (enemy.x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, AGENT_COLOR, rect)
        else:
            # If the enemy is dead, remove it from the enemies list
            enemies.remove(enemy)


# Function to move enemy towards player with collision check
def move_enemy_towards_player(enemy, player):
    player_x, player_y = player.x, player.y  # Get player's position
    
    if enemy.x < player_x:
        new_enemy_x = enemy.x + 1
    elif enemy.x > player_x:
        new_enemy_x = enemy.x - 1
    else:
        new_enemy_x = enemy.x

    if enemy.y < player_y:
        new_enemy_y = enemy.y + 1
    elif enemy.y > player_y:
        new_enemy_y = enemy.y - 1
    else:
        new_enemy_y = enemy.y

    # Check for collision with the player
    if (new_enemy_x, new_enemy_y) == (player_x, player_y):
        print("Enemy hit player!")
        enemy.take_damage(10)
        
        player.take_damage(5)  # Apply damage to the player instance
        
        print("Enemy health:", enemy.health)
        print("Player health:", player.health)

    # Check for collision with other enemies or obstacles
    if not is_enemy_collision(new_enemy_x, new_enemy_y, enemies):
        enemy.x, enemy.y = new_enemy_x, new_enemy_y  # Update enemy position if no collision



# Collision function that excludes dead enemies
def is_enemy_collision(x, y, enemies):
    # Only check for collisions with live enemies
    return any((enemy.x == x and enemy.y == y) for enemy in enemies if enemy.is_alive())
