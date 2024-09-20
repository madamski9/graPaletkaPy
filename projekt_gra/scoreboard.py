import pygame
from settings import WIN, HEIGHT, WIDTH, FONT
from draw_button import draw_button
from bubble_sort import bubble_sort
from load_and_save_scores import load_scores, load_nickname, save_best_score
from best_score import import_best_score

def show_scoreboard(ending_score):
    selected_button = 0
    buttons = ["MENU"]
        
    run = True
    sorted_ending_score = bubble_sort(load_scores())
    nickname = load_nickname()
    best_score = dict(zip(nickname, sorted_ending_score))
    save_best_score(best_score)

    for nick in load_nickname():
        nickname2 = nick

    while run:
        WIN.fill("white")
        for i, button in enumerate(buttons):
            if i == selected_button:
                color = "red"
            else:
                color = "black"
            button_y = (HEIGHT+200)/2 + i * 60
            draw_button(button, button_y, color)

        start_y = 100
        counter = 1
        for score in sorted_ending_score[:10]:
            score_text = FONT.render(f"{counter}. {nickname2}'s score: {str(score)}", 1, "black")
            WIN.blit(score_text, (WIDTH/2 - score_text.get_width()/2 - 130, start_y))
            import_best_score()

            start_y += 30
            counter += 1

        scoreboard_text = FONT.render("SCOREBOARD", 1, "black")
        WIN.blit(scoreboard_text, (WIDTH/2 - scoreboard_text.get_width()/2 - 130, 60))
        best_scores_text = FONT.render("BEST SCORES", 1, "black")
        WIN.blit(best_scores_text, (WIDTH/2 - scoreboard_text.get_width()/2 + 130, 60))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selected_button == 0:
                        from game_menu import menu
                        menu(ending_score)
                        run = False

    return run