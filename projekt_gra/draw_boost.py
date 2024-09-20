from settings import WIDTH, HEIGHT

def draw_boost(player, x, y, boosts, score):
    boosts_to_remove = []
    for boost in boosts:

        boost['x'] += boost['speed_x']
        boost['y'] += boost['speed_y']

        if boost['x'] <= 0 or boost['x'] >= WIDTH - 40:
            boost['direction_x'] *= -1
            boost['speed_x'] = boost['speed'] * boost['direction_x']

        # odbicie od paletki
        if (
            x <= boost['x'] and
            x + player.get_width() >= boost['x'] and
            y <= boost['y'] and
            y + player.get_height() >= boost['y']
        ):
            boosts_to_remove.append(boost)
            score += 5

        if boost['y'] <= 0:
            boost['direction_y'] *= -1
            boost['speed_y'] = boost['speed'] * boost['direction_y']
        
        if boost['y'] >= HEIGHT - 40:
            boosts_to_remove.append(boost)

    for boost in boosts_to_remove:
        boosts.remove(boost)

    return score

