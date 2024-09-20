from load_and_save_scores import load_best_score
from settings import WIN, WIDTH, FONT
from slownik_sort import sorted_slownik

def import_best_score():
    best_score = load_best_score()
    best_score = sorted_slownik(best_score)

    start_y = 100
    counter = 1
    for key, value in best_score.items():
        best_score_text = FONT.render(f"{counter}. {key}'s score: {value}", 1, "black")
        WIN.blit(best_score_text, (WIDTH/2 - best_score_text.get_width()/2 + 130, start_y))     

        start_y += 30
        counter += 1
    