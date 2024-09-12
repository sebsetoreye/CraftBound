import pygame
import sys


from .game_functions import *
from .game_variables import *

pygame.init()




# Main function
def main():
    change_screen_size()
    player_x, player_y = 5, 5  # Starting position of the agent
    output1 = 0   # Generic output label

    # Button positions
    button_quit_rect = pygame.Rect(new_WINDOW_WIDTH - BUTTON_SIZE * 2 - 10, 5, BUTTON_SIZE, BUTTON_SIZE)
    button_b_rect = pygame.Rect(new_WINDOW_WIDTH - BUTTON_SIZE - 5, 5, BUTTON_SIZE, BUTTON_SIZE)
    
    


    # Main game loop
    while True:
        draw_grid()
        
        draw_agent(player_x, player_y)
        draw_room(0, 0, 40, 15)

        # Display Output1 at the top margin
        font = pygame.font.SysFont(None, 24)
        output_text = font.render(f'Output1: {output1}', True, (255, 255, 255))
        screen.blit(output_text, (5, 5))

        # Check if buttons are clicked
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        is_button_quit_clicked = button_quit_rect.collidepoint(mouse_pos) and mouse_pressed[0]
        is_button_b_clicked = button_b_rect.collidepoint(mouse_pos) and mouse_pressed[0]

        # Display buttons with click feedback
        draw_button('Quit', button_quit_rect.x, button_quit_rect.y, BUTTON_SIZE, is_button_quit_clicked)
        draw_button('B', button_b_rect.x, button_b_rect.y, BUTTON_SIZE, is_button_b_clicked)

        # Display instructions at the bottom margin
        controls_text = font.render('Use Arrow Keys to Move or Click to Interact', True, (255, 255, 255))
        screen.blit(controls_text, (5, new_WINDOW_HEIGHT - CELL_SIZE + 5))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                new_x, new_y = player_x, player_y
                if event.key == pygame.K_LEFT:
                    new_y = max(0, player_y - 1)
                elif event.key == pygame.K_RIGHT:
                    new_y = min(COLS - 1, player_y + 1)
                elif event.key == pygame.K_UP:
                    new_x = max(0, player_x - 1)
                elif event.key == pygame.K_DOWN:
                    new_x = min(ROWS - 1, player_x + 1)

                # Check for collision before moving
                if not is_collision(new_x, new_y):
                    player_x, player_y = new_x, new_y
                    


            # Handle mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_quit_rect.collidepoint(mouse_pos):
                    print("Button A clicked!")
                elif button_b_rect.collidepoint(mouse_pos):
                    print("Button B clicked!")
                
                grid_pos = get_grid_position(mouse_pos)
                if grid_pos:
                    gx, gy = grid_pos
                    print(f"Grid {gx},{gy} clicked")

        pygame.time.delay(100)  # Control the speed of movement
