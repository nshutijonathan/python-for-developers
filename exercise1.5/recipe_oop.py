class Recipe(object):
    """Recipe object"""

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = None

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "easy"
            print(self.difficulty)
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "medium"
            print(self.difficulty)
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
            print(self.difficulty)
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "hard"
            print(self.difficulty)

    def __str__(self):
        return self.name

    def ingredients(self):

        return self.ingredients

    def difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            print("true")
            return True
        else:
            return False

    def update_all_ingredients(self, new_ingredients):
        if new_ingredients not in self.ingredients:
            self.ingredients.append(new_ingredients)
        return self.ingredients

    def recipe_search(self, data, search_term):
        for item in data:
            if item.search_ingredient(search_term):
                return item
        else:
            return False


tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs",
              "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Bananas Smoothie", [
                         "Banana", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
recipes_list = [tea, coffee, cake, banana_smoothie]
