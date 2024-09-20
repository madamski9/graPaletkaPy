import pygame
import pytest
from game_objects import initialize_player

WIDTH, HEIGHT = 500, 700

def test_initialize_player():
    pygame.init()
    player, x, y, PLAYER_VEL, x_change = initialize_player()

    assert x == WIDTH * 0.35
    assert y == 560
    assert PLAYER_VEL == 15
    assert x_change == 0

    pygame.quit()



