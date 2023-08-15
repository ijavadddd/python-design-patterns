'''
The provided example illustrates the implementation of the Singleton design pattern in Python. The Singleton pattern ensures that 
a class has only one instance and provides a global point of access to that instance throughout the entire application.

Here's an explanation of the components and their roles in the example:

1. **`Singleton` Class**:
   - This class is designed to enforce the Singleton pattern.
   - It overrides the `__call__` method to control the instantiation process.
   - The `_instance` class variable keeps track of the single instance of the class.

2. **Usage**:
   - Two instances of the `Singleton` class (`singleton1` and `singleton2`) are created.
   - The comparison `singleton1 is singleton2` is used to check if both instances are the same (which is true in this case).

In the provided example, the `Singleton` class ensures that only a single instance of itself is created. When attempting to 
create a new instance, the overridden `__call__` method checks if an instance already exists. 
If not, it creates the instance; otherwise, it returns the existing instance.

The Singleton pattern is useful in scenarios where you want to control access to a single instance of a class, such as managing
global resources, configurations, or shared objects that should have a single point of access throughout your application.
'''
from typing import Any


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs) -> Any:
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance
    

class Somethings(metaclass=Singleton):
    pass


singleton1 = Somethings()
singleton2 = Somethings()

print(singleton1 is singleton2)