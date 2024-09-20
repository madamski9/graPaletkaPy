import pytest
import pygame
import random
from game_objects import create_ball

WIDTH = 500 
HEIGHT = 700

def test_create_ball():
    pygame.init() 
    ball = create_ball()

    assert 0 <= ball['x'] < WIDTH - 40
    assert 0 <= ball['y'] < HEIGHT // 2 - 40
    assert ball['speed_x'] == 8
    assert ball['speed_y'] == 8
    assert ball['direction_x'] == 1
    assert ball['direction_y'] == 1
    assert ball['speed'] == 8

    pygame.quit()  