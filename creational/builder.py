'''
Certainly! The example I provided is about implementing the Builder design pattern in Python
for creating a simplified database table definition. The goal is to demonstrate how the 
Builder pattern can be used to construct complex objects (in this case, a table with columns) 
step by step, while separating the construction process from the client code.

Here's a breakdown of the components and their roles in the example:

1. **`TableBuilder` (Builder)**:
   - This is the builder class that provides methods to construct a complex object
    (a database table with columns).
   - It has methods like `add_column()` to add columns and `add_primary_key()` to set the
    primary key.
   - It maintains a reference to the product (`Table`) being built.

2. **`Table` (Product)**:
   - This is the product class that represents the complex object being built 
    (a database table).
   - It holds information about the table's name, columns, and primary key.

3. **`Column`**:
   - This is a simple class representing a column in a database table. It stores the column 
    name and data type.

In this example, the `TableBuilder` acts as the builder, guiding the creation of a `Table` 
object step by step. The client code (main program) uses the builder to create a table 
definition, adding columns and setting a primary key. The builder encapsulates the 
construction logic, abstracting away the complexity from the client.

The benefits of using the Builder pattern in this scenario include:

- Simplifying the creation of complex objects by breaking down the process into manageable 
steps.
- Separating the construction process from the client code, promoting a cleaner and more 
maintainable design.
- Allowing the creation of different variations of the same complex object (different table 
structures) using the same builder interface.

Remember, the Builder pattern is particularly useful when the construction process of a 
complex object involves multiple steps or when you want to create different configurations of 
the same object without exposing the underlying details to the client.
'''

class TableBuilder:
    def __init__(self, name):
        self.table = Table(name)

    def add_column(self, column_name, column_type):
        self.table.add_column(Column(column_name, column_type))

    def add_primary_key(self, column_name):
        self.table.set_primary_key(column_name)

    def change_column_name(self, column_name, new_column_name):
        raise NotImplementedError
    
    def get_table(self):
        return self.table

class Table:
    def __init__(self, name):
        self.name = name
        self.columns = []
        self.primary_key = None
    
    def add_column(self, column):
        self.columns.append(column)

    def set_primary_key(self, column_name):
        self.primary_key = column_name

    def __str__(self):
        table_info = f"Table: {self.name}\n"
        for column in self.columns:
            table_info += f"- {column}\n"
        if self.primary_key:
            table_info += f"Primary Key: {''.join(self.primary_key)}"
        return table_info
    
class Column:
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type
    
    def __str__(self):
        return f"{self.name} ({self.data_type})"
    

def main():
    '''
    >>> my_table = TableBuilder('user')
    >>> my_table.add_column('id', 'int')
    >>> my_table.add_column('name','string')
    >>> my_table.add_primary_key('id')
    >>> print(my_table.get_table())
    Table: user
    - id (int)
    - name (string)
    Primary Key: id
    '''
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
