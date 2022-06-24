"""
Facade Design Pattern (Involves Information Hiding),
the members in Facade are made private to abstract
the complexities in the subsystems

Structural Pattern
"""

class problem1:
    @staticmethod
    def method():
        return 1

class problem2:
    @staticmethod
    def method():
        return 2

class problem3:
    @staticmethod
    def method():
        return 3

class Facade:
    def __init__(self):
        self.prob1 = problem1()
        self.prob2 = problem2()
        self.prob3 = problem3()

    def call_method(self):
        combine = 0
        combine += self.prob1.method()
        combine += self.prob2.method()
        combine += self.prob3.method()
        return combine

if __name__ == "__main__":
    facade = Facade()
    print(facade.call_method())