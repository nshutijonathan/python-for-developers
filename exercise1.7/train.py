def calculate_difficulty(cooking_time, ingredients):
    difficulty = ""
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "easy"
        print(difficulty)
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "medium"
        print(difficulty)
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
        print(difficulty)
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "hard"
        print(difficulty)
    else:
        difficulty = "unknown"

    return difficulty


calculate_difficulty(5, "nsnsnbb")
