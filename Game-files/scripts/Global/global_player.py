import pygame
from scripts.game_screens.game_variables import CELL_SIZE, MARGIN_ROWS, COLS, ROWS
from scripts.game_screens.game_functions import is_collision, screen, sys


PLAYER_COLOR = (255, 100, 0)


class Player:
    def __init__(self, x, y, direction="up", health=100):
        self.x = x
        self.y = y
        self.health = health
        self.direction = direction
    
    # Method to check if the player is alive
    def is_alive(self):
        return self.health > 0
    
    # Method to reduce health of the player
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0


def draw_player(player):
    if player.is_alive():
        # Draw the player if alive
        rect = pygame.Rect(player.y * CELL_SIZE, (player.x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, PLAYER_COLOR, rect)


def handle_player_movement(event, player):
    new_x, new_y = player.x, player.y

    if event.key == pygame.K_LEFT:
        new_y = max(0, player.y - 1)  # Move left (decrease y)
        player.direction = "left"
    elif event.key == pygame.K_RIGHT:
        new_y = min(COLS - 1, player.y + 1)  # Move right (increase y)
        player.direction = "right"
    elif event.key == pygame.K_UP:
        new_x = max(0, player.x - 1)  # Move up (decrease x)
        player.direction = "up"
    elif event.key == pygame.K_DOWN:
        new_x = min(ROWS - 1, player.x + 1)  # Move down (increase x)

    # Check for collisions with walls first
    if not is_collision(new_x, new_y):
        player.x, player.y = new_x, new_y  # Update player position
    else:
        print("Collision detected, cannot move!")  # Debug message for collision

    # Check for door collision after moving

def handle_mouse_click(mouse_pos, button_quit_rect):
    if button_quit_rect.collidepoint(mouse_pos):
        print("Quit button clicked!")
        pygame.quit()
        sys.exit()