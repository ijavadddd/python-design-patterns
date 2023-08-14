'''
This example illustrates the use of the Prototype design pattern in Python. The Prototype pattern 
is a creational pattern that allows you to create new objects by copying an existing object
(prototype) rather than creating them from scratch. This can be particularly useful when the cost
of creating an object is high or when you need to create variations of objects quickly.

Here's a breakdown of the components and their roles in this example:

1. **`Shape` (Abstract Base Class)**:
   - This is an abstract base class (ABC) that defines a common interface for all shapes.
   - It declares an abstract method `clone()`, which should be implemented by its concrete subclasses.

2. **`Circle` and `Square` (Concrete Classes)**:
   - These are concrete subclasses of `Shape` that implement the `clone()` method.
   - Each subclass initializes its properties (radius or side) and then creates a new instance of the
    same class with the same properties using the `__dict__` attribute.

3. **Prototype Creation**:
   - Instances of `Circle` and `Square` are created as prototype objects
    (`circle_prototype` and `Square_prototype`), representing initial shapes.
   - The `clone()` method in each prototype class uses the `__dict__` attribute to create a 
   new instance with the same attributes.

4. **Object Creation Using Prototypes**:
   - The `clone()` method is used to create new instances of shapes (`circle1` and `square1`) 
    based on the prototype objects.
   - The new instances have the same attributes as the prototypes.

In summary, this example demonstrates how the Prototype pattern allows you to create new 
instances of shapes by cloning existing prototype objects. It's useful when you want to create new 
objects with the same initial properties as existing ones, thus reducing the overhead of object 
creation and improving performance.

Please note that while the example demonstrates the concept of the Prototype pattern, the specific 
implementation may not provide a deep copy, especially if the shape objects contain 
references to other objects. In a production scenario, you might need to handle deep copying or 
other considerations depending on your requirements.
'''
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def clone(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def clone(self):
        return self.__class__(**self.__dict__)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def clone(self):
        return self.__class__(**self.__dict__)
    

circle_prototype = Circle(radius=5)
Square_prototype = Square(side=10)

circle1 = circle_prototype.clone()
square1 = Square_prototype.clone()

print(circle1.radius)
print(square1.side)