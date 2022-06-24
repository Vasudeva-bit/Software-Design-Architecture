from abc import ABCMeta, abstractstaticmethod

class ISubjects(metaclass=ABCMeta):
    def print_sub():
        """Implemented in the child class"""

class Math(ISubjects):
    def __init__(self, marks):
        self.marks = marks
    def print_sub(self):
        print(f"Math: {self.marks}")

class CS(ISubjects):
    def __init__(self, marks):
        self.marks = marks
    def print_sub(self):
        print(f"CS: {self.marks}")

class BonusTotal(ISubjects):

    def __init__(self, marks):
        self.objs = []
        self.marks = marks
        self.tot = marks

    def addSub(self, obj):
        self.objs.append(obj)
        self.tot += obj.marks

    def print_sub(self):
        for i in self.objs:
            i.print_sub()
        print("Total: ", self.tot)

if __name__ == "__main__":
    math = Math(99)
    math.print_sub()

    cs = CS(98)
    cs.print_sub()

    tot = BonusTotal(99)
    tot.addSub(math)
    tot.print_sub()

    tot = BonusTotal(97)
    tot.addSub(math)
    tot.addSub(cs)
    tot.print_sub()