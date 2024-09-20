def save_scores(ending_score, filename="highscores.txt"):
    with open(filename, "w") as file:
        for score in ending_score:
            file.write(f"{score}\n")

def load_scores(filename="highscores.txt"):
    try:
        with open(filename, "r") as file:
            scores = []
            for line in file:
                stripped_line = line.strip()
                score = int(stripped_line)
                scores.append(score)
            return scores
    except FileNotFoundError:
        return []
    
def save_nickname(nickname, filename="nicknames.txt"):
    with open(filename, "w") as file:
        for nick in nickname:
            file.write(f"{nick}")
        file.write("\n")

def load_nickname(filename="nicknames.txt"):
    with open(filename, "r") as file:
        nicks = []
        for line in file:
            stripped_line = line.strip()
            nick = str(stripped_line)
            nicks.append(nick)
        return nicks

def save_best_score(best_score, filename="best_score.txt"):
    with open(filename, "a") as file:
        for key, value in best_score.items():
            file.write(f"{key}: {value}")
        file.write('\n')

def load_best_score(filename="best_score.txt"):
    with open(filename, "r") as file:
        best_scores = {}
        for line in file:
            try:
                key, value = line.strip().split(':')
                best_scores[key] = int(value)
            except ValueError:
                continue
        return best_scores



