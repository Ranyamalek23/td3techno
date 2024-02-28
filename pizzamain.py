from CartePizzeria import CartePizzeria
from CartePizzeriaException import CartePizzeriaException
from Pizza import Pizza


if __name__ == "__main__":
    # Création de quelques pizzas
    pizza1 = Pizza("Margherita", ["Tomato sauce", "Mozzarella", "Basil"], 8.99)
    pizza2 = Pizza("Pepperoni", ["Tomato sauce", "Pepperoni", "Mozzarella"], 9.99)

    # Création de la carte de la pizzeria
    carte_pizzeria = CartePizzeria()

    # Ajout de pizzas à la carte
    carte_pizzeria.add_pizza(pizza1)
    carte_pizzeria.add_pizza(pizza2)

    # Affichage du nombre de pizzas sur la carte
    print("Nombre de pizzas sur la carte:", carte_pizzeria.nb_pizzas())

    # Suppression d'une pizza de la carte
    carte_pizzeria.remove_pizza("Margherita")

    # Affichage du nombre de pizzas sur la carte après suppression
    print("Nombre de pizzas sur la carte après suppression:", carte_pizzeria.nb_pizzas())

    # Tentative de suppression d'une pizza qui n'existe pas sur la carte
    try:
        carte_pizzeria.remove_pizza("Quattro Stagioni")
    except CartePizzeriaException as e:
        print("Exception lors de la suppression:", e)