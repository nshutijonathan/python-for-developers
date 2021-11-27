import pickle


def display_recipe(my_recipes):
    print("dumped_pickled", my_recipes)
    return my_recipes


pickled = open('recipesdetails.bin', 'rb')
dumped_pickled = pickle.load(pickled)


def search_ingredient(data):
    for ingredient in data['ingredients']:
        if ingredient == 'chocolate':
            print("Recipe", data['name'])
            print("Cooking Time", data['cooking_time'])
            print("Ingredients:", data['ingredients'])


display_recipe(dumped_pickled)
search_ingredient(dumped_pickled)
