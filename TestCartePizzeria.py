import unittest
from unittest.mock import Mock
from your_module import CartePizzeria, CartePizzeriaException, Pizza

class TestCartePizzeria(unittest.TestCase):
    def test_is_empty(self):
        carte_pizzeria = CartePizzeria()
        self.assertTrue(carte_pizzeria.is_empty())

        pizza_mock = Mock(spec=Pizza)
        carte_pizzeria.add_pizza(pizza_mock)
        self.assertFalse(carte_pizzeria.is_empty())

    def test_nb_pizzas(self):
        carte_pizzeria = CartePizzeria()
        self.assertEqual(carte_pizzeria.nb_pizzas(), 0)

        pizza_mock1 = Mock(spec=Pizza)
        pizza_mock2 = Mock(spec=Pizza)
        carte_pizzeria.add_pizza(pizza_mock1)
        carte_pizzeria.add_pizza(pizza_mock2)
        self.assertEqual(carte_pizzeria.nb_pizzas(), 2)

    def test_add_pizza(self):
        carte_pizzeria = CartePizzeria()
        pizza_mock = Mock(spec=Pizza)
        carte_pizzeria.add_pizza(pizza_mock)
        self.assertIn(pizza_mock, carte_pizzeria.pizzas)

    def test_remove_pizza(self):
        carte_pizzeria = CartePizzeria()
        pizza_mock1 = Mock(spec=Pizza)
        pizza_mock1.name = "Margherita"
        pizza_mock2 = Mock(spec=Pizza)
        pizza_mock2.name = "Pepperoni"
        carte_pizzeria.add_pizza(pizza_mock1)
        carte_pizzeria.add_pizza(pizza_mock2)

        carte_pizzeria.remove_pizza("Margherita")
        self.assertNotIn(pizza_mock1, carte_pizzeria.pizzas)
        self.assertIn(pizza_mock2, carte_pizzeria.pizzas)

        with self.assertRaises(CartePizzeriaException):
            carte_pizzeria.remove_pizza("Quattro Stagioni")


if __name__ == '__main__':
    unittest.main()
