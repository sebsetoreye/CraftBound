import pygame
from scripts.game_screens.game_variables import *
from scripts.gui_screens.start_screen_files.start_screen_variables import *
from scripts.game_screens.game_functions import *
from scripts.Global.global_variables import *

PLAYER_COLOR = (255, 100, 0)


class Player:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
    
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
    new_x, new_y = player.x, player.y  # Get player's current position

    if event.key == pygame.K_LEFT:
        new_y = max(0, player.y - 1)  # Move left
    elif event.key == pygame.K_RIGHT:
        new_y = min(COLS - 1, player.y + 1)  # Move right
    elif event.key == pygame.K_UP:
        new_x = max(0, player.x - 1)  # Move up
    elif event.key == pygame.K_DOWN:
        new_x = min(ROWS - 1, player.x + 1)  # Move down

    # Check for collision before moving
    if not is_collision(new_x, new_y):
        player.x, player.y = new_x, new_y  # Update player's position


def handle_mouse_click(mouse_pos, button_quit_rect, button_b_rect):
    if button_quit_rect.collidepoint(mouse_pos):
        print("Quit button clicked!")
        pygame.quit()
        sys.exit()
    elif button_b_rect.collidepoint(mouse_pos):
        print("Button B clicked!")

    grid_pos = get_grid_position(mouse_pos)
    if grid_pos:
        gx, gy = grid_pos
        print(f"Grid {gx},{gy} clicked")

