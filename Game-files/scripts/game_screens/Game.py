import pygame
import sys
import random

from scripts.game_screens.game_functions import *
from scripts.game_screens.game_variables import *
from scripts.Global.global_functions import *
from scripts.Global.global_variables import *
from scripts.Global.global_enemies import *
from scripts.Global.global_player import *
from scripts.Global.global_weapons import *
from scripts.Global.weapons import *

def main():

    
    change_screen_size()
    frame_counter = 0


    # Initialize the player at a specific position
    player = Player(x=7, y=19)

    # Boolean to track whether the player is in the start room
    in_start_room = True

    # Load initial room (start room)
    current_room = start_room

    # Main game loop
    while True:
        # Clear the screen and draw the grid
        draw_grid()
        frame_counter += 1
        #draw_score(score, 100, 5)  # Draw the current score

        # Draw the current room
        current_room()  # Draw the current room walls and doors

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Handle player movement
                room_changed = handle_player_movement(event, player)  # Check if room change is needed

                # Only spawn enemies after leaving the start room
                if in_start_room and room_changed:
                    in_start_room = False  # Player has now left the start room
                    print("Player left the start room, spawning enemies.")
                    current_room = random_room()  # Load a random room
                    load_room(current_room)  # Set up the new room
                    reset_enemies()  # Spawn random enemies

                # Check for room changes when not in the start room
                elif room_changed and is_door_collision(player.x, player.y):
                    print("Room changed, loading new random room!")
                    current_room = random_room()  # Load a random room
                    load_room(current_room)  # Set up the new room
                    player.x, player.y = 7, 19
                    reset_enemies()  # Spawn random enemies for the new room

                # Attack an enemy
                if event.key == pygame.K_a:
                    hit_enemy_with_weapon(player, enemies, sword)

        # Draw the player and enemies
        draw_player(player)
        draw_enemy(enemies)
        draw_health_display(player.health, 10, 10)

        # Move enemies every few frames
        if frame_counter % enemy_move_delay == 0:
            move_all_enemies(enemies, player)

        pygame.display.flip()  # Update the screen
        pygame.time.delay(100)  # Control the speed of movement
