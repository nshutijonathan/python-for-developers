recipes_list = []
ingredients_list = []


def take_recipe():
    name = str(input("What is the recipe name? "))
    cooking_time = int(input("How long does it take to cook? "))
    ingredients = str(input("What are the ingredients? ")).split()
    recipe = {'name': name, "cooking_time": cooking_time,
              "ingredients": ingredients}

    for(ingredient) in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
    for(rec) in recipes_list:
        if rec['cooking_time'] < 10 and len(rec['ingredients']) < 2:
            difficulty = ''
            difficulty = difficulty+'Easy'
            print("difficulty leve", difficulty)
        elif rec['cooking_time'] < 10 and len(rec['ingredients']) >= 4:
            difficulty = ''
            difficulty = difficulty+'Medium'
            print("difficulty leve", difficulty)
        elif rec['cooking_time'] >= 10 and len(rec['ingredients']) < 4:
            difficulty = ''
            difficulty = difficulty+'Intermediate'
            print("difficulty leve", difficulty)
        elif rec['cooking_time'] >= 10 and len(rec['ingredients']) >= 4:
            difficulty = ''
            difficulty = difficulty+'Hard'
            print("difficulty leve", difficulty)
    return recipe


n = int(input("How many recipes do you want to enter? "))
for i in range(n):
    for value in recipes_list:
        print("Recipes", value['name'])
        print("Cooking Time", value['cooking_time'])
        print("Ingredients:", value['ingredients'])
    take_recipe()
for items in ingredients_list:
    print("Ingredients Available Acrross All Recipes", items)
