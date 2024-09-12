import pygame
from scripts.game_screens.game_functions import *
from scripts.game_screens.game_variables import *


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
    #draw_room(0, 0, 40, 15)

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
