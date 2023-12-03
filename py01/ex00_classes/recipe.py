class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        try:
            cooking_lvl = int(cooking_lvl)
            if cooking_lvl < 1 or cooking_lvl > 5:
                raise ValueError("Cooking level must be between 1 and 5")
        except ValueError:
            print("Cooking level must be an integer")
        try:
            cooking_time = int(cooking_time)
            if cooking_time < 0:
                raise ValueError("Cooking time must be positive")
        except ValueError:
            print("Cooking time must be an integer")
        if len(ingredients) == 0:
            raise ValueError("Ingredients cannot be empty")
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            raise ValueError("Recipe type must be starter, lunch or dessert")    
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        txt = f"Name: {self.name}\nCooking level: {self.cooking_lvl}\nCooking time: {self.cooking_time}\nIngredients: {self.ingredients}\nDescription: {self.description}\nRecipe type: {self.recipe_type}"
        return txt