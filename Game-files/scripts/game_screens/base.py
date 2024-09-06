import pygame
import sys


from scripts.main.main_functions import *
from scripts.main.main_variables import *


# Main function
def main():
    x, y = 5, 10  # Starting position of the agent
    output1 = 0   # Generic output label

    # Button positions
    button_quit_rect = pygame.Rect(WINDOW_WIDTH - BUTTON_SIZE * 2 - 10, 5, BUTTON_SIZE, BUTTON_SIZE)
    button_b_rect = pygame.Rect(WINDOW_WIDTH - BUTTON_SIZE - 5, 5, BUTTON_SIZE, BUTTON_SIZE)

    # Main game loop
    while True:
        draw_grid()
        draw_agent(x, y)

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
        screen.blit(controls_text, (5, WINDOW_HEIGHT - CELL_SIZE + 5))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    y = max(0, y - 1)
                elif event.key == pygame.K_RIGHT:
                    y = min(COLS - 1, y + 1)
                elif event.key == pygame.K_UP:
                    x = max(0, x - 1)
                elif event.key == pygame.K_DOWN:
                    x = min(ROWS - 1, x + 1)

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
