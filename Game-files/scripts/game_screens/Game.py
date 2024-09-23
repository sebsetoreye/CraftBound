import pygame
import sys
import random

from scripts.game_screens.game_functions import *
from scripts.game_screens.game_variables import *
from scripts.game_screens.rooms.rooms import *
from scripts.Global.global_functions import *
from scripts.Global.global_variables import *
from scripts.Global.global_enemies import *
from scripts.Global.global_player import *
from scripts.Global.global_weapons import *
from scripts.Global.weapons import *

pygame.init()


def main():
    change_screen_size()
    frame_counter = 0
    output1 = 0  # Generic output label

    # Button positions
    button_quit_rect = pygame.Rect(new_WINDOW_WIDTH - BUTTON_SIZE * 2 - 10, 5, BUTTON_SIZE, BUTTON_SIZE)
    button_b_rect = pygame.Rect(new_WINDOW_WIDTH - BUTTON_SIZE - 5, 5, BUTTON_SIZE, BUTTON_SIZE)

    # Initialize the player at a specific position
    player = Player(x=7, y=19)

    # Random enemy start position and list initialization
    enemies = [Enemy(random.randint(0, ROWS - 1), random.randint(0, COLS - 1))]

    # Main game loop
    while True:
        draw_grid()
        frame_counter += 1

        dev_room()  # Presumably drawing or logic related to the development room

        # Draw the player and enemies
        draw_player(player)
        draw_enemy(enemies)

# Move enemies every few frames
        if frame_counter % enemy_move_delay == 0:
            move_all_enemies(enemies, player)

        # Check for player collision with walls
        if is_collision(player.x, player.y):
            print("Player hit a wall!")

        # Check for player collision with doors

        # Check if buttons are clicked
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        is_button_quit_clicked = button_quit_rect.collidepoint(mouse_pos) and mouse_pressed[0]
        is_button_b_clicked = button_b_rect.collidepoint(mouse_pos) and mouse_pressed[0]

        # Display buttons with click feedback
        draw_button('Quit', button_quit_rect.x, button_quit_rect.y, BUTTON_SIZE, is_button_quit_clicked)
        draw_button('B', button_b_rect.x, button_b_rect.y, BUTTON_SIZE, is_button_b_clicked)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                handle_player_movement(event, player)  # Separate function to handle movement
                
                if event.key == pygame.K_a:
                    hit_enemy_with_weapon(player, enemies, sword)


            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                handle_mouse_click(mouse_pos, button_quit_rect, button_b_rect)
            
            

        pygame.display.flip()  # Update the screen
        pygame.time.delay(100)  # Control the speed of movement
