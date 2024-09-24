import pygame
from scripts.game_screens.game_variables import CELL_SIZE, MARGIN_ROWS, COLS, ROWS, BUTTON_TEXT_COLOR
from scripts.game_screens.game_functions import is_collision, screen, sys, random_room, is_door_collision


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
        new_y = max(0, player.y - 1)
        player.direction = "left"
    elif event.key == pygame.K_RIGHT:
        new_y = min(COLS - 1, player.y + 1)
        player.direction = "right"
    elif event.key == pygame.K_UP:
        new_x = max(0, player.x - 1)
        player.direction = "up"
    elif event.key == pygame.K_DOWN:
        new_x = min(ROWS - 1, player.x + 1)
        player.direction = "down"

    # Check for wall collisions
    if not is_collision(new_x, new_y):
        player.x, player.y = new_x, new_y
    else:
        print("Collision detected, cannot move!")

    # Check for door collisions
    if is_door_collision(new_x, new_y):
        print("Door collision detected, loading random room!")
        return True  # Indicate that we need to load a new room

    return False  # No room change

def handle_mouse_click(mouse_pos, button_quit_rect):
    if button_quit_rect.collidepoint(mouse_pos):
        print("Quit button clicked!")
        pygame.quit()
        sys.exit()




def draw_health_display(player_health, x, y):
    # Render the player's health text
    font = pygame.font.SysFont(None, 24)
    health_text = f'HP: {player_health}'  # Format health display
    text_render = font.render(health_text, True, BUTTON_TEXT_COLOR)
    text_rect = text_render.get_rect(topleft=(x, y))  # Position at (x, y)
    
    # Draw health text on the screen
    screen.blit(text_render, text_rect)