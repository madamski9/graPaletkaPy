import pygame
import random
from settings import WIN, WIDTH, FONT, HEIGHT
from game_objects import create_ball

def impediments(elapsed_time, balls):
    screen_shake_intensity = 2
    screen_shake = 0
    global color

    # poziom 1
    if elapsed_time >= 0 and elapsed_time <= 3:
        color = "white"
        notification_text = FONT.render("Poziom 1", 1, "black")
        WIN.blit(notification_text, (WIDTH/2 - notification_text.get_width()/2, HEIGHT/2 - notification_text.get_height()/2))
        boost_text = FONT.render("+5pkt", 1, "black")
        WIN.blit(boost_text, (WIDTH/2 - boost_text.get_width()/2, HEIGHT/2 - boost_text.get_height()/2 - 100))
        boost_image = pygame.transform.scale(pygame.image.load('boost.png'), (35, 35))
        WIN.blit(boost_image, (WIDTH/2 - boost_text.get_width()/2 - 40, HEIGHT/2 - boost_text.get_height()/2 - 107))

    # poziom 2
    if elapsed_time >= 10:
        balls[0]['speed'] = 10
        screen_shake = 560

    if elapsed_time >= 10 and elapsed_time <= 13:
        color = (228, 171, 171)
        notification_text = FONT.render("Poziom 2", 1, "black")
        WIN.blit(notification_text, (WIDTH/2 - notification_text.get_width()/2, HEIGHT/2 - notification_text.get_height()/2))

    # poziom 3
    if elapsed_time >= 20 and len(balls) == 1:
        balls.append(create_ball())
        balls[1]['speed'] = 10
        screen_shake = 560
        screen_shake_intensity *= 2
    
    if elapsed_time >= 20 and elapsed_time <= 23:
        color = (185, 73, 73)
        notification_text = FONT.render("Poziom 3", 1, "black")
        WIN.blit(notification_text, (WIDTH/2 - notification_text.get_width()/2, HEIGHT/2 - notification_text.get_height()/2))

    # poziom 4
    if elapsed_time >= 30:
        for ball in balls:
            ball['speed'] = 10
        screen_shake = 560
        screen_shake_intensity *= 3
    
    if elapsed_time >= 30 and elapsed_time <= 33:
        color = (94, 9, 9)
        notification_text = FONT.render("Poziom 4", 1, "white")
        WIN.blit(notification_text, (WIDTH/2 - notification_text.get_width()/2, HEIGHT/2 - notification_text.get_height()/2))

    # poziom 5
    if elapsed_time >= 40 and len(balls) == 2:
        balls.append(create_ball())

    if elapsed_time >= 40 and elapsed_time <= 43:
        color = (68, 1, 1)
        notification_text = FONT.render("Poziom 5", 1, "white")
        WIN.blit(notification_text, (WIDTH/2 - notification_text.get_width()/2, HEIGHT/2 - notification_text.get_height()/2))
    
    # poziom 6
    if elapsed_time >= 65 and len(balls) == 3:
        balls.append(create_ball())

    if elapsed_time >= 65 and elapsed_time <= 70:
        color = (25, 1, 1)
        notification_text = FONT.render("Poziom 6", 1, "white")
        WIN.blit(notification_text, (WIDTH/2 - notification_text.get_width()/2, HEIGHT/2 - notification_text.get_height()/2))

    # screen shake
    if screen_shake > 0:
        screen_shake -= 1
    
    render_offset = [0, 0]
    if screen_shake:
        render_offset[0] = random.randint(-screen_shake_intensity, screen_shake_intensity) 
        render_offset[1] = random.randint(-screen_shake_intensity, screen_shake_intensity) 

    WIN.blit(WIN, render_offset)
    
    pygame.display.update()

    WIN.fill(color) 
