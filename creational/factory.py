'''
The example provided illustrates the use of the Factory design pattern in a deployment
management scenario. The Factory pattern is used to create different types of deployment 
services, each responsible for deploying software applications to various environments 
(e.g., cloud servers, local servers).


The benefits of using the Factory pattern in this example include:

- Separating the object creation logic from the client code, making the client more
focused on using the services rather than creating them.
- Enabling the addition of new types of deployment services without 
modifying the existing client code.
- Promoting a more modular and maintainable design by centralizing object creation.

In the provided example, the client code creates instances of different deployment services 
using the Factory (`DeploymentService`). It then utilizes these services to deploy an 
application. The Factory pattern helps manage the creation of complex objects with varying
functionalities in a flexible and organized manner.
'''

from typing import Protocol

class DeploymentService(Protocol):
    def deploy(self):
        raise NotImplementedError()


class CloudDeployment:
    def deploy(self):
        return 'cloud-deploy'
    


class LocalDeployment:
    def deploy(self):
        return 'local-deploy'


def get_deployment_service(deployment_type: str) -> DeploymentService:
    deployment_typs = {
        'cloud': CloudDeployment,
        'local': LocalDeployment
    }
    return deployment_typs[deployment_type]()

def main():
    '''
    >>> print(get_deployment_service('cloud').deploy())
    cloud-deploy
    >>> print(get_deployment_service('local').deploy())
    local-deploy
    '''
    if __name__ == "__main__":
        import doctest
        doctest.testmod()