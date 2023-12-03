from recipe import Recipe
from book import Book

ratatouille = Book("Ratatouille")
cake = Recipe("Cake", 3, 60, ["eggs", "flour", "sugar"], "A delicious cake.", "dessert")
cookie = Recipe("Cookie", 3, 60, ["eggs", "flour", "sugar"], "A delicious cake.", "dessert")
ratatouille.add_recipe(cake)
ratatouille.add_recipe(cookie)
#txt = ratatouille.get_recipe_by_name(cake)
#print(txt)
xx = ratatouille.get_recipes_by_types("dessert")
for i in xx:
    print(i)



