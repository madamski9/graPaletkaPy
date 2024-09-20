import pygame
import random
import time
from settings import WIDTH, HEIGHT

def initialize_player():
    player = pygame.transform.scale(pygame.image.load('paletka2.png'), (150, 150))
    x = (WIDTH * 0.35)
    y = 560
    PLAYER_VEL = 15
    x_change = 0

    return player, x, y, PLAYER_VEL, x_change

def initialize_objects_and_time():
    balls = [create_ball()]
    boosts = [create_boost()]

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    ball_time = 0
    boost_time = 0

    return balls, clock, start_time, elapsed_time, ball_time, boosts, boost_time

def create_ball():
    ball = {
        'ball': pygame.transform.scale(pygame.image.load('ball.png'), (40, 40)),
        'x': random.randint(0, WIDTH-40),
        'y': random.randint(0, HEIGHT //2 -40),
        'speed_x': 8,
        'speed_y': 8,
        'direction_x': 1,
        'direction_y': 1,
        'speed': 8
    }
    return ball

def create_boost():
    boost = {
        'boost' : pygame.transform.scale(pygame.image.load('boost.png'), (25, 25)),
        'x': random.randint(0, WIDTH-40),
        'y': random.randint(0, HEIGHT //2 -40),
        'speed_x': 5,
        'speed_y': 5,
        'direction_x': 1,
        'direction_y': 1,
        'speed': 5
    }
    return boost