cookbook = {}
cookbook["bocadillo"] = ("jamón, pan, queso y tomate", "almuerzo", "10 minutos")
cookbook["tarta"] = ("harina, azúcar y huevos", "postre", "60 minutos")
cookbook["ensalada"] = ("aguacate, rúcula, tomates y espinacas", "almuerzo", "15 minutos")


def print_recetas_cookbook():
    '''
    Imprime las recetas del cookbook
    '''
    print("Recetas :")
    index = 0;
    for key in cookbook:
        print(f"{index}:\t{key}")
        index += 1

def print_detallas(receta):
    '''
    Imprime los detalles de una receta
    '''
    index = 0
    for key in cookbook:
        if key == receta:
            break
        index += 1
    if index == len(cookbook):
        print("Sorry, this recipe does not exist.")
        return
    print(f"\nReceta: {receta}")
    print(f"   Ingredientes: {cookbook[receta][0]}")
    print(f"   Tipo: {cookbook[receta][1]}")
    print(f"   Tiempo de preparación: {cookbook[receta][2]}")

def del_receta(receta):
    '''
    Elimina una receta del cookbook
    '''
    index = 0
    for key in cookbook:
        if key == receta:
            break
        index += 1
    if index == len(cookbook):
        print("Sorry, this recipe does not exist.")
        return
    del cookbook[receta]

def add_receta():
    '''
    Añade una receta al cookbook
    '''
    nombre = input("Nombre de la receta:\n")
    ingredientes = input("Ingredientes:\n")
    tipo = input("Tipo:\n")
    tiempo = input("Tiempo de preparación:\n")
    cookbook[nombre] = (ingredientes, tipo, tiempo)

print("Welcome to the Pyhton Cookbook !")
print("List of available options:\n   1: Add a recipe\n   2: Delete a recipe\n   3: Print a recipe\n   4: Print the cookbook\n   5: Quit", end="\n\n")

while (True):
    option = input("Please select an option:\n")
    print()
    try:
        option = int(option)
    except:
        print("Please enter a number")
        continue
    if option == 0 | option > 5:
        print("Sorry, this option does not exist.")
        continue
    elif option == 1:
        add_receta()
    elif option == 2:
        del_receta(input("Which recipe do you want to delete ?\n"))
    elif option == 3:
        print_detallas(input("Which recipe do you want to print ?\n"))
    elif option == 4:
        print_recetas_cookbook()
    elif option == 5:
        print("Cookbook closed. Goodbye !")
        break
    print()