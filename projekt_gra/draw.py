from settings import WIN, FONT, WIDTH

def draw(player, x, y, elapsed_time, balls, score, boosts):
    tmp_color = ""
    WIN.blit(player, (x,y))
    for ball in balls:
        WIN.blit(ball['ball'], (ball['x'], ball['y']))

    for boost in boosts:
        WIN.blit(boost['boost'], (boost['x'], boost['y']))

    if elapsed_time <= 30:
        tmp_color = "black"
    else:
        tmp_color = "white"

    time_text = FONT.render(f"Czas: {round(elapsed_time)}s", 1, tmp_color)
    WIN.blit(time_text, (10,10))

    score = FONT.render(f"Wynik: {score}", 1, tmp_color)
    WIN.blit(score, (WIDTH-score.get_width()-10, 10))
    