

from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+pymysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    cooking_time = Column(Integer)
    difficulty = Column(String(50))
    ingredients = Column(String(255))

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.name}),difficulty={self.difficulty}"

    def __str__(self) -> str:
        return super().__str__()

    def calculate_difficulty(self, cooking_time, ingredients):
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

    def return_ingredients_as_list(self):
        recipes_list = session.query(Recipe).all()
        print("recipes_list", recipes_list[2].ingredients)
        if len(recipes_list) == 0:
            return []
        else:
            for recipe in recipes_list:
                ingredients_list = recipe.ingredients.split(",")
                return ingredients_list

    def create_recipe(self):
        name = str(input("Enter the name of the recipe: ")),
        if len(name) > 50:
            print("Name must be less than 50 characters")
            return
        cooking_time = int(input("Enter the cooking time: "))
        if type(cooking_time) != int:
            print("Cooking time must be an integer")
            return
        igredients = []
        ingredients_number = int(input("Enter the number of ingredients:"))
        if type(ingredients_number) != int:
            print("Number of ingredients must be an integer")
            return
        for i in range(ingredients_number):
            igredients.append(str(input("Enter the ingredient: ")))
        igredients = ','.join(igredients)

        recipe = Recipe(
            name=name,
            cooking_time=cooking_time,
            ingredients=igredients,
            difficulty=self.calculate_difficulty(cooking_time, igredients))
        session.add(recipe)
        session.commit()

    def search_by_ingredients(self):
        ingredients = str(input("Enter the ingredients: "))
        recipes = session.query(Recipe).filter(
            Recipe.ingredients.like(f"%{ingredients}%")).all()
        if len(recipes) == 0:
            print("No recipes found")
        else:
            for recipe in recipes:
                print(recipe.name)

    def edit_recipe(self):
        recipe_id = int(input("Enter the recipe id: "))
        recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
        if recipe is None:
            print("No recipe found")
            return
        name = str(input("Enter the name of the recipe: "))
        if len(name) > 50:
            print("Name must be less than 50 characters")
            return
        cooking_time = int(input("Enter the cooking time: "))
        if type(cooking_time) != int:
            print("Cooking time must be an integer")
            return
        igredients = []
        ingredients_number = int(input("Enter the number of ingredients:"))
        if type(ingredients_number) != int:
            print("Number of ingredients must be an integer")
            return
        for i in range(ingredients_number):
            igredients.append(str(input("Enter the ingredient: ")))
        igredients = ','.join(igredients)

        recipe.name = name
        recipe.cooking_time = cooking_time
        recipe.ingredients = igredients
        recipe.difficulty = self.calculate_difficulty(cooking_time, igredients)
        session.commit()

    def delete_recipe(self):
        recipe_id = int(input("Enter the recipe id: "))
        recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
        if recipe is None:
            print("No recipe found")
            return
        session.delete(recipe)
        session.commit()


Base.metadata.create_all(engine)
my_recipe = Recipe()
session.query(my_recipe.create_recipe())
session.query(my_recipe.return_ingredients_as_list())
