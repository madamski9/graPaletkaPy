import pygame
import pytest
import time
from game_objects import initialize_objects_and_time

WIDTH, HEIGHT = 500, 700

def test_initialize_objects_and_time():
    pygame.init()
    balls, clock, start_time, elapsed_time, ball_time, boosts, boost_time = initialize_objects_and_time()

    assert len(balls) > 0
    assert start_time > 0
    assert elapsed_time == 0
    assert ball_time == 0

    pygame.quit()

    