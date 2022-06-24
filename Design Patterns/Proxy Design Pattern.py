from abc import ABCMeta, abstractstaticmethod

class ISubject(metaclass=ABCMeta):
    def secret_marks():
        """The secret_marks class is implemented in the child classes"""

class Math(ISubject):
    def __init__(self, marks):
        self.marks = marks

    def secret_marks(self):
        print(f"Math: {self.marks}")

class secret_proxy(ISubject):
    def __init__(self):
        self.math = Math(98)

    def secret_marks(self):
        self.math.secret_marks()

if __name__ == "__main__":
    obj = secret_proxy()
    obj.secret_marks()