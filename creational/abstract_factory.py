'''
**What is this pattern about?

Certainly! The provided example demonstrates the implementation of the Abstract Factory design
pattern in Python within the context of an online restaurant ordering system. The goal is to 
create an architecture that can produce two types of food (Pizza and Burger) and two types of 
drinks (Soda and Water) for customer orders.

Here's a breakdown of the example:

1. **Abstract Factory (`RestaurantFactory`)**: This class defines the abstract methods 
`create_food` and `create_drink`, which act as factory methods for creating food and drink 
objects.

2. **Concrete Factories (`PizzaFactory` and `BurgerFactory`)**: These classes inherit from the 
`RestaurantFactory` and provide specific implementations for creating food and drink objects. For 
example, `PizzaFactory` creates `Pizza` and `Soda` objects, while `BurgerFactory` creates 
`Burger` and `Water` objects.

3. **Abstract Products (`Food` and `Drink`)**: These classes define the abstract methods 
`prepare` and `serve`, respectively, which represent the preparation and serving actions for food 
and drink items.

4. **Concrete Products (`Pizza`, `Burger`, `Soda`, and `Water`)**: These classes inherit from the 
corresponding abstract product classes and provide concrete implementations for the `prepare` and 
`serve` methods. Each product represents a specific type of food or drink.

5. **Order Placement (`place_order` function)**: This function takes a factory as an argument and
uses it to create both a food item and a drink item. It then returns the preparation and serving 
messages for the ordered items.

In essence, the Abstract Factory pattern allows you to create families of related objects (food 
and drink items in this case) without specifying their concrete classes. This separation of 
object creation from the client code enables you to easily switch between different types of 
foods and drinks while maintaining a consistent interface for ordering and serving them.

'''
import doctest


class ResturantFactory:
    def order_food(self):
        pass
    
    def order_drink(self):
        pass

class PizzaFactory(ResturantFactory):
    def order_food(self):
        return Pizza()
    
    def order_drink(self):
        return Soda()

class BurgerFactory(ResturantFactory):
    def order_food(self):
        return Burger()
    
    def order_drink(self):
        return Water()

class Food:
    def prepare(self):
        pass

class Drink:
    def serve(self):
        pass

class Pizza(Food):
    def prepare(self):
        return 'your pizza will be prepared soon'

class Burger(Food):
    def prepare(self):
        return 'your burger will be prepared soon'

class Soda(Drink):
    def serve(self):
            return 'your soda will be served soon'

class Water(Drink):
    def serve(self):
        return 'your water will be served soon'
    
def place_order(factory):
    food = factory.order_food()
    drink = factory.order_drink()
    print(food.prepare())
    print(drink.serve())

def main():
    '''
    # Order pizza and soda
    >>> order_pizza = place_order(PizzaFactory())
    your pizza will be prepared soon
    your soda will be served soon

    # Order burger and water
    >>> order_burger = place_order(BurgerFactory())
    your burger will be prepared soon
    your water will be served soon
    '''
    if __name__ == '__main__':
        doctest.testmod()