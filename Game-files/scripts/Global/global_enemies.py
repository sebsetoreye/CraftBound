import pygame
import random
from scripts.game_screens.game_variables import *
from scripts.gui_screens.start_screen_files.start_screen_variables import *
from scripts.game_screens.game_functions import *
from scripts.Global.global_variables import *
from scripts.Global.global_player import Player



# Base Enemy class to manage position, health, and movement
class Enemy:
    def __init__(self, x, y, health=100, damage=10):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
    
    # Method to check if the enemy is alive
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
    
    # Base movement towards the player (can be overridden)
    def move_towards_player(self, player, enemies):
        player_x, player_y = player.x, player.y  # Get player's position

        # Standard enemy movement (1 step closer to player)
        new_enemy_x, new_enemy_y = self.x, self.y
        if self.x < player_x:
            new_enemy_x = self.x + 1
        elif self.x > player_x:
            new_enemy_x = self.x - 1

        if self.y < player_y:
            new_enemy_y = self.y + 1
        elif self.y > player_y:
            new_enemy_y = self.y - 1

        # Check if the new position is the player's position
        if (new_enemy_x, new_enemy_y) == (player_x, player_y):
            print("Enemy hit player!")
            player.take_damage(self.damage)  # Apply damage to the player
            print("Player health:", player.health)
        else:
            # Check for collision with other enemies
            if not is_enemy_collision(new_enemy_x, new_enemy_y, enemies):
                self.x, self.y = new_enemy_x, new_enemy_y  # Move enemy if no collision
                print(f"Enemy moved to ({self.x}, {self.y})")

# Specialized FastEnemy with faster movement
class FastEnemy(Enemy):
    def __init__(self, x, y, health=50, damage=5):
        super().__init__(x, y, health, damage)

    # Overrides the base movement to move twice as fast
    def move_towards_player(self, player, enemies):
        for _ in range(2):  # Moves two steps toward the player each turn
            super().move_towards_player(player, enemies)

# TankEnemy moves slower but has more health and deals more damage
class TankEnemy(Enemy):
    def __init__(self, x, y, health=200, damage=20):
        super().__init__(x, y, health, damage)

    # Could include slower movement or movement with additional checks if needed
    def move_towards_player(self, player, enemies):
        # Move every other turn (or custom logic for slow movement)
        super().move_towards_player(player, enemies)

# Collision function that excludes dead enemies
def is_enemy_collision(x, y, enemies):
    return any(enemy.x == x and enemy.y == y for enemy in enemies if enemy.is_alive())

# Function to move all enemies
def move_all_enemies(enemies, player):
    for enemy in enemies:
        enemy.move_towards_player(player, enemies)

def draw_enemy(enemies):
    for enemy in enemies[:]:
        if enemy.is_alive():
            # Define a color based on the enemy type
            if isinstance(enemy, FastEnemy):
                color = (255, 0, 0)  # Red for FastEnemy
            elif isinstance(enemy, TankEnemy):
                color = (0, 255, 0)  # Green for TankEnemy
            else:
                color = AGENT_COLOR  # Default color for base Enemy
            
            # Draw the enemy rectangle based on its type and position
            rect = pygame.Rect(enemy.y * CELL_SIZE, (enemy.x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
        else:
            # If the enemy is dead, increase the score and remove the enemy
            enemies.remove(enemy)



def reset_enemies():
    enemies.clear()  # Clear existing enemies
    enemy_classes = [Enemy, FastEnemy, TankEnemy]  # List of enemy classes to choose from

    # Reinitialize enemies based on the new room specifics
    for _ in range(3):  # Example: spawn 3 random enemies in the new room
        enemy_class = random.choice(enemy_classes)  # Randomly select an enemy class
        # Create a new enemy at random positions (make sure they are valid positions)
        x = random.randint(0, ROWS - 1)
        y = random.randint(0, COLS - 1)
        enemies.append(enemy_class(x, y))  # Instantiate and add the new enemy
