import pygame
from settings import HEIGHT, WIDTH, WIN, FONT
from load_and_save_scores import save_nickname

def blit_nickname():
    run = True
    user_nickname = ""
    nick = False

    while run:
        WIN.fill("white")
        
        nick_text = FONT.render("WPROWADZ NICK: ", 1, "black")
        WIN.blit(nick_text, (WIDTH/2 - nick_text.get_width()/2 - 50, 300))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_nickname = user_nickname[:-1]
                    text_rect = pygame.Rect(WIDTH/2 - enter_nickname.get_width()/2 + 135, 300, 200, 50)
                    WIN.fill("white", text_rect)
                if event.key == pygame.K_RETURN:
                    if len(user_nickname) == 0:
                        save_nickname("NoName")
                    else:
                        save_nickname(user_nickname)
                    nick = True
                    break
                elif event.key != pygame.K_BACKSPACE:
                    user_nickname += event.unicode

        enter_nickname = FONT.render(user_nickname, True, (0,0,0))
        WIN.blit(enter_nickname, (WIDTH/2 - enter_nickname.get_width()/2 + 135, 300))

        pygame.display.update()

        if nick:
            return True

    return run
