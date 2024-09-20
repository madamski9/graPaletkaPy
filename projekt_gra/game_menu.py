import pygame
from settings import HEIGHT, WIDTH, WIN, FONT
from scoreboard import show_scoreboard
from draw_button import draw_button

def menu(ending_score):
    selected_button = 0
    buttons = ["START", "SCOREBOARD", "EXIT"]
    run = True

    while run:
        WIN.fill("white")
        
        for i, button in enumerate(buttons):
            if i == selected_button:
                color = "red"
            else:
                color = "black"
            button_y = (HEIGHT-70)/2 + i * 60
            draw_button(button, button_y, color)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and event.key != pygame.K_RETURN:
                    selected_button = (selected_button + 1) % len(buttons)
                if event.key == pygame.K_UP and event.key != pygame.K_RETURN:
                    selected_button = (selected_button - 1) % len(buttons)
                if event.key == pygame.K_RETURN:
                    if selected_button == 0:
                        return True
                    elif selected_button == 1:
                        show_scoreboard(ending_score)
                    elif selected_button == 2:
                        pygame.quit()

    return run
