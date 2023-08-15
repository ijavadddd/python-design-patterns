'''
The provided example demonstrates the use of the Borg design pattern (also known as Shared State or Monostate) in Python. 
The Borg pattern is a behavioral design pattern that allows multiple instances of a class to share a common state while retaining 
their individual identities. Unlike the Singleton pattern, where only one instance of a class exists, in the Borg pattern, 
multiple instances coexist and share the same state.

Here's an explanation of the example and its components:

1. **`WebServerConfigBorg` Class**:
   - This class represents a configuration manager for web servers.
   - It utilizes the Borg pattern to share configuration settings among instances.
   - The `_shared_state` class variable is used to maintain the shared state among instances.
   - The `set_config` method allows setting the configuration (port and root directory).
   - The `display_config` method displays the current configuration.

2. **Usage**:
   - Two instances of the `WebServerConfigBorg` class (`server1` and `server2`) are created.
   - The `set_config` method is used to set the configuration for each instance.
   - The `display_config` method is used to display the configuration for each instance.

In this example, the Borg pattern enables multiple instances of `WebServerConfigBorg` to share configuration settings.
When a configuration is changed in one instance, the change is reflected across all instances.

**Real-World Scenario: Web Server Configuration Management**

Imagine you are building a web server management system where each web server has a common set of configurations, 
such as the port number and root directory. Using the Borg pattern, you can ensure that changes made to the configuration of
one web server are applied to all web servers, ensuring consistency across the system.

The Borg pattern is particularly useful when you want to share state among instances while allowing them to have their own identities.
It can be beneficial in scenarios where objects need to share common resources or settings, ensuring that changes made to one 
instance are propagated to others.

Please note that the Borg pattern is less common and less widely used than other design patterns like Singleton or Factory, 
but it can be handy in specific situations where shared state and individual identity are required.
'''

class WebServerConfighBorg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

    def set_config(self, port, root_directory):
        self.port = port
        self.root_directory = root_directory
    
    def display_config(self):
        print(f'Port: {self.port}\nRoot Directory: {self.root_directory}')


# Usage
server1 = WebServerConfighBorg()
server2 = WebServerConfighBorg()

server1.set_config(8080, "/var/www")
server2.display_config()  # Output: Port: 8080, Root Directory: /var/www
print('-------------')
server2.set_config(8000, "/opt/web")
server1.display_config()  # Output: Port: 8000, Root Directory: /opt/web
print('********')
server2.display_config()  # Output: Port: 8000, Root Directory: /opt/web