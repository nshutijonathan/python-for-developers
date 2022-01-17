import pickle

# pickled = open('recipe_binary.bin', 'rb')
# dumped_pickled = pickle.load(pickled)
# print("dumped_pickled", dumped_pickled)


recipes_list = []


def take_recipes():
    name = str(input("What is the recipe name? "))
    cooking_time = int(input("How long does it take to cook? "))
    ingredients = str(input("What are the ingredients? ")).split()
    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {'name': name, "cooking_time": cooking_time,
              "ingredients": ingredients, 'difficulty': difficulty}
    recipes_list.append(recipe)
    return recipe


def calc_difficulty(time, ingredients):
    if time < 10 and len(ingredients) < 4:
        difficulty = ''
        difficulty = difficulty+'Easy'
        print("difficulty leve", difficulty)
    elif time < 10 and len(ingredients) >= 4:
        difficulty = ''
        difficulty = difficulty+'Medium'
        print("difficulty leve", difficulty)
    elif time >= 10 and len(ingredients) < 4:
        difficulty = ''
        difficulty = difficulty+'Intermediate'
        print("difficulty leve", difficulty)
    elif time >= 10 and len(ingredients) >= 4:
        difficulty = ''
        difficulty = difficulty+'Hard'
        print("difficulty leve", difficulty)


def display(file):
    data = []
    for line in file:
        # Removing newline characters
        line = line.rstrip("\n")
        data.append(line)
        return data


filename = input("Enter the filename where you've stored your recipes: ")
try:
    pickled = open('recipesdetails.bin', 'rb')
    dumped_pickled = pickle.load(pickled)
    display(dumped_pickled)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
except:
    print("An unexpected error occurred.")
else:
    dumped_pickled.close()
finally:
    print("Goodbye!")

take_recipes()
my_file_dumped_binary = open('recipesdetails.bin', 'wb')
recipes_list.append(pickle.dump(recipes_list, my_file_dumped_binary))
my_file_dumped_binary.close()

# recipe = {
#     'name': 'Tea',
#     'ingredients': ['tea_leaves,water,sugar'],
#     'cooking_time': '5mins',
#     'difficulty': 'easy'
# }
# my_file = open('recipe_binary.bin', 'wb')
# pickle.dump(recipe, my_file)
# my_file.close()

# my_pickeddata = pickle.load(open('recipe_binary.bin', 'rb'))
# print(my_pickeddata)
