from datetime import datetime

class Book:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
    last_update = datetime.now()
    def get_recipe_by_name(self, name):
        return(f"Recipes for {name.name}:\n{name}")
    
    def get_recipes_by_types(self, recipe_type):
        return self.recipes_list[recipe_type]
            
    
    def add_recipe(self, recipe):
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        print(f"Recipe for {recipe.name} added to the book")