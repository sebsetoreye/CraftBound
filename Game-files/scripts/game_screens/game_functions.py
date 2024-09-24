
import pygame
import sys
import math
import random

from .game_variables import *
from scripts.gui_screens.start_screen_files.start_screen_variables import *
from scripts.Global.global_functions import *

background_image = pygame.image.load('Game-files/sprites/floor/floor.png')
background_image = pygame.transform.scale(background_image, (new_WINDOW_WIDTH, new_WINDOW_HEIGHT))  # Scale it to the window size


def change_screen_size():
    global screen
    screen = pygame.display.set_mode((new_WINDOW_WIDTH, new_WINDOW_HEIGHT))



def draw_grid():
    # Draw the background image
    screen.blit(background_image, (0, 0))  # Draw the image at the top-left corner
    for x in range(0, new_WINDOW_WIDTH, CELL_SIZE):
        for y in range(MARGIN_ROWS * CELL_SIZE, (ROWS + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)


# Function to draw the agent/player
def draw_agent(x, y):
    rect = pygame.Rect(y * CELL_SIZE, (x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, AGENT_COLOR, rect)



# Function to get grid coordinates from mouse position
def get_grid_position(mouse_pos):
    mouse_x, mouse_y = mouse_pos
    grid_x = (mouse_y // CELL_SIZE) - MARGIN_ROWS
    grid_y = mouse_x // CELL_SIZE
    if 0 <= grid_x < ROWS and 0 <= grid_y < COLS:
        return grid_x, grid_y
    return None


# Function to draw buttons
#// Need to change 
def draw_button(text, x, y, size, is_clicked):
    color = BUTTON_CLICK_COLOR if is_clicked else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, size, size))
    font = pygame.font.SysFont(None, 24)
    text_render = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_render.get_rect(center=(x + size // 2, y + size // 2))
    screen.blit(text_render, text_rect)


# Function to draw the wall
def draw_wall(x, y):
    rect = pygame.Rect(y * CELL_SIZE, (x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, Wall_Color, rect)
    walls.append((x, y))  # Add wall to the list

def draw_door(x, y):
    rect = pygame.Rect(y * CELL_SIZE, (x + MARGIN_ROWS) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, Wall_Color, rect)
    doors.append((x, y))  # Add wall to the list

#Draw room
def draw_room(start_x, start_y, width, height):
    for x in range(start_x, start_x + width):
        draw_wall(start_y, x)  # Top wall
        draw_wall(start_y + height - 1, x)  # Bottom wall
    for y in range(start_y, start_y + height):
        draw_wall(y, start_x)  # Left wall
        draw_wall(y, start_x + width - 1)  # Right wall

#Wall/map build Tool
def Draw_wall_horizontal(start_x, end_x, y_pos):
    for x in range(start_x, start_x + end_x):
        draw_wall(y_pos, x)

def Draw_wall_vertical(start_y, end_y, x_pos):
    for y in range(start_y, start_y + end_y):
        draw_wall(y, x_pos)  

#Draw doors
def Draw_door_horizontal(start_x, end_x, y_pos):
    for x in range(start_x, start_x + end_x):
        draw_door(y_pos, x)

def Draw_door_vertical(start_y, end_y, x_pos):
    for y in range(start_y, start_y + end_y):
        draw_door(y, x_pos) 

#Collision detection
def is_collision(x, y):
    return (x, y) in walls

def is_door_collision(x, y):
    return (x, y) in doors


def random_room():
    # Add all room functions to a list
    rooms = [room_1, room_2, room_3]  # Add more room functions as needed
    # Randomly select a room function
    selected_room = random.choice(rooms)
    return selected_room  # Return the selected room function


def load_room(room_function):
    # This function will load a given room function
    walls.clear()  # Clear existing walls
    doors.clear()  # Clear existing doors
    room_function()


def dev_room():
    draw_room(0, 0, 40, 15)
    Draw_door_horizontal(1, 5, 1)

def start_room():
    Draw_wall_horizontal(0, 18, 0)
    Draw_wall_horizontal(21, 40, 0)
    Draw_wall_horizontal(0, 18, 1)
    Draw_wall_horizontal(21, 40, 1)
    Draw_wall_horizontal(0, 18, 2)
    Draw_wall_horizontal(21, 40, 2)
    Draw_wall_horizontal(0, 18, 3)
    Draw_wall_horizontal(21, 40, 3)
    Draw_wall_horizontal(0, 18, 4)
    Draw_wall_horizontal(21, 40, 4)
    Draw_wall_horizontal(0, 17, 5)
    Draw_wall_horizontal(22, 40, 5)

    Draw_wall_horizontal(0, 17, 9)
    Draw_wall_horizontal(22, 40, 9)
    Draw_wall_horizontal(0, 18, 10)
    Draw_wall_horizontal(21, 40, 10)
    Draw_wall_horizontal(0, 18, 11)
    Draw_wall_horizontal(21, 40, 11)
    Draw_wall_horizontal(0, 18, 12)
    Draw_wall_horizontal(21, 40, 12)
    Draw_wall_horizontal(0, 18, 13)
    Draw_wall_horizontal(21, 40, 13)
    Draw_wall_horizontal(0, 18, 14)
    Draw_wall_horizontal(21, 40, 14)

def room_1():


    #top of the room
    Draw_wall_horizontal(0, 17, 0)
    Draw_wall_horizontal(20, 40, 0)

    #Left wall
    Draw_wall_vertical(0, 7, 0)
    Draw_wall_vertical(10, 5, 0)

    #Right wall
    Draw_wall_vertical(0, 15, 39)

    #Floor
    Draw_wall_horizontal(0, 40, 15)

def room_2():

    #roof
    Draw_wall_horizontal(0, 17, 0)
    Draw_wall_horizontal(20, 40, 0)
    #floor
    Draw_wall_horizontal(0, 40, 14)
    #left wall
    Draw_wall_vertical(0, 15, 0)
    #right wall
    Draw_wall_vertical(0, 7, 39)
    Draw_wall_vertical(10, 5, 39) 

def room_3():
    #roof
    Draw_wall_horizontal(0, 4, 0)
    Draw_wall_horizontal(4, 3, 0)
    Draw_wall_horizontal(10, 3, 0)
    Draw_wall_horizontal(16, 3, 0)
    Draw_wall_horizontal(22, 3, 0)
    Draw_wall_horizontal(28, 3, 0)
    Draw_wall_horizontal(34, 6, 0)
    #floor
    Draw_wall_horizontal(0, 4, 14)
    Draw_wall_horizontal(4, 3, 14)
    Draw_wall_horizontal(10, 3, 14)
    Draw_wall_horizontal(16, 3, 14)
    Draw_wall_horizontal(22, 3, 14)
    Draw_wall_horizontal(28, 3, 14)
    Draw_wall_horizontal(34, 6, 14)
    #walls
    Draw_wall_vertical(0, 15, 0)
    Draw_wall_vertical(0, 15, 39)
