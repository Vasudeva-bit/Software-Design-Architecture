from abc import ABCMeta, abstractstaticmethod
from re import I

class IBlog(metaclass=ABCMeta):
    def subscribe(self):
        """Implemented by the child class"""

    def unsubscribe(self):
        """Implemented by the child class"""

    def notify(self):
        """Implemented by the child class"""

class BlogA(IBlog):
    def __init__(self):
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)
        print(f"{observer.name} is added!")

    def unsubscribe(self, observer):
        self.observers.remove(observer)
        print(f"{observer.name} is removed!")

    def notify(self):
        for observer in self.observers:
            observer.notify()

class IObserver(metaclass=ABCMeta):
    def notify(self):
        """Implemented by the child class"""
        
    def getState(self):
        """Implemented by the child class"""

class Observer(IObserver):
    def __init__(self, name, blog):
        self.name = name
        blog.subscribe(self)

    def notify(self):
        print("Here is the notification!, ", self.name)

if __name__ == "__main__":
    blog = BlogA()
    observer1 = Observer("Vasudeva", blog)
    observer2 = Observer("Nidhi", blog)
    update = bool(int(input("Any update on blog [0/1]: ")))
    
    if(update):
        blog.notify()

    blog.unsubscribe(observer1)