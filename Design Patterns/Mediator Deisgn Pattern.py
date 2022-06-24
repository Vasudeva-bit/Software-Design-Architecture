from abc import ABCMeta, abstractstaticmethod
from email.policy import Compat32

class IMediator(metaclass=ABCMeta):
    def addComp():
        """Implemented by the child class"""

    def notify():
        """Implemented by the child class"""

class IComponent(metaclass=ABCMeta):
    def notify():
        """Implemented by the child components"""

    def recieve():
        """Implemented by the child components"""


class Mediator(IMediator):
    def __init__(self):
        self.Comps = []
    def addComp(self, component):
        self.Comps.append(component)
    def notify(self, component):
        for Comp in self.Comps:
            if Comp != component:
                Comp.recieve()


class Component1(IComponent):
    def __init__(self, mediator):
        self.mediator = mediator
    def notify(self):
        print("Component1 is in Active")
        self.mediator.notify(self)
    def recieve(self):
        print("Component1 is in Inactive Mode")


class Component2(IComponent):
    def __init__(self, mediator):
        self.mediator = mediator
    def notify(self):
        print("Component2 is in Active")
        self.mediator.notify(self)
    def recieve(self):
        print("Component2 is in Inactive Mode")

if __name__ == "__main__":
    mediator = Mediator()
    Comp1 = Component1(mediator)
    Comp2 = Component2(mediator)
    mediator.addComp(Comp1)
    mediator.addComp(Comp2)
    Comp1.notify()
