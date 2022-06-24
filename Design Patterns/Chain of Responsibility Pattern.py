from abc import ABCMeta, abstractstaticmethod

class IDespenser(metaclass=ABCMeta):
    def dispenser():
        """dispenser is implemented in the child class"""

    def call_next():
        """call_next is implemented in the child class"""

class Dispenser50(IDespenser):
    def __init__(self, amount):
        self.amount = amount
        if self.amount > 50:
            self.dispenser()
        else:
            self.call_next()
    
    def dispenser(self):
        print("The number of 50s are ", self.amount//50)
        if(self.amount%50 > 0):
            self.call_next()

    def call_next(self):
        Dispenser20(self.amount%50)

class Dispenser20(IDespenser):
    def __init__(self, amount):
        self.amount = amount
        if self.amount > 20:
            self.dispenser()
        else:
            self.call_next()
    
    def dispenser(self):
        print("The number of 20s are ", self.amount//20)
        if(self.amount%20 > 0):
            self.call_next()

    def call_next(self):
        Dispenser10(self.amount%20)

class Dispenser10(IDespenser):
    def __init__(self, amount):
        self.amount = amount
        if self.amount > 10:
            self.dispenser()
        else:
            self.call_next()
    
    def dispenser(self):
        print("The number of 10s are ", self.amount//10)
        self.call_next()

    def call_next(self):
        print("The number of 10s are ", self.amount//10)
        if(self.amount%10 == 0):
            print("All the money is dispensed")
        else:
            print("The money, not multiple of 10 can't be dispensed!")


class client:
    def __init__(self, amount):
        Dispenser50(amount)


if __name__ == "__main__":
    client(int(input("Enter the amount to be dispensed: ")))