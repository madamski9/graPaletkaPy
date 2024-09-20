import pygame
import time
from settings import WIDTH, HEIGHT, FPS, WIN, FONT
from game_menu import menu, draw_button
from game_objects import initialize_player, initialize_objects_and_time
from impediments import impediments
from draw import draw
from load_and_save_scores import save_scores
from nickname import blit_nickname
from draw_boost import draw_boost
from game_objects import create_boost
pygame.font.init()
pygame.init()
pygame.display.set_caption("gra paletka")
ending_score = []
nickname = []

if __name__ == "__main__":
    blit_nickname()

def main():
    run = True
    player, x, y, PLAYER_VEL, x_change = initialize_player()
    balls, clock, start_time, elapsed_time, ball_time, boosts, _ = initialize_objects_and_time()
    score = 0
    selected_button = 0
    buttons = ["RESTART", "MENU", "WYJSCIE"]
    last_boost_time = time.time()

    while run:
        clock.tick(FPS)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - PLAYER_VEL >= -33:
            x_change = -PLAYER_VEL
        elif keys[pygame.K_RIGHT] and x + PLAYER_VEL + player.get_width() <= WIDTH+34:
            x_change = PLAYER_VEL
        else:
            x_change = 0
        x += x_change

        current_time = time.time()
        if current_time - last_boost_time >= 10: 
            boosts.append(create_boost())
            last_boost_time = current_time
        
        score = draw_boost(player, x, y, boosts, score)

        for ball in balls:
            ball['x'] += ball['speed_x']
            ball['y'] += ball['speed_y']
            if ball['x'] <= 0 or ball['x'] >= WIDTH - 40:
                ball['direction_x'] *= -1
                ball['speed_x'] = ball['speed'] * ball['direction_x']
            # odbicie od paletki
            if (
                x <= ball['x'] and
                x + player.get_width() >= ball['x'] and
                y <= ball['y'] and
                y + player.get_height() >= ball['y'] and
                elapsed_time - ball_time >= 0.2
            ):
                ball['direction_y'] *= -1  
                ball['speed_y'] = ball['speed'] * ball['direction_y']
                score += 1
                ball_time = elapsed_time
            if ball['y'] <= 0:
                ball['direction_y'] *= -1
                ball['speed_y'] = ball['speed'] * ball['direction_y']

            # przegrana
            if ball['y'] >= HEIGHT - 40:
                waiting_for_input = True
                ending_score.append(score)
                save_scores(ending_score)
                tmp_color = ""
                while waiting_for_input:
                    
                    if elapsed_time <= 30:
                        tmp_color = "black"
                    else:
                        tmp_color = "white"

                    lost_text = FONT.render("PRZEGRALES", 1, tmp_color)
                    WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, 200))
                    score_text = FONT.render(f"TWOJ WYNIK TO: {score}", 1, tmp_color)
                    WIN.blit(score_text, (WIDTH/2 - lost_text.get_width()/2 - 30, 250))

                    for i, button in enumerate(buttons):
                        if i == selected_button:
                            color = "red"
                        else:
                            color = tmp_color
                        button_y = (HEIGHT+40)/2 + i * 60
                        draw_button(button, button_y, color)

                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                selected_button = (selected_button + 1) % len(buttons)
                            if event.key == pygame.K_UP:
                                selected_button = (selected_button - 1) % len(buttons)
                            if event.key == pygame.K_RETURN:
                                if selected_button == 0:
                                    from main import main
                                    main()
                                    waiting_for_input = False
                                if selected_button == 1:
                                    menu(ending_score)
                                    waiting_for_input = False
                                elif selected_button == 2:
                                    run = False
                                    waiting_for_input = False

        impediments(elapsed_time, balls)
        draw(player, x, y, elapsed_time, balls, score, boosts)
    pygame.quit()
if __name__ == "__main__":
    main()
