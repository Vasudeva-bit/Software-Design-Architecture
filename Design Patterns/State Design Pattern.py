from abc import ABCMeta

class IVendingMachine(metaclass=ABCMeta):
    def insertCash(self):
        """Implemented by the child classes"""
    
    def RequestProduct(self):
        """Implemented by the child classes"""

    def ejectCash(self):
        """Implemented by the child classes"""

class VendingMachine(IVendingMachine):
    def __init__(self):
        self.Idle = IdleState(self)
        self.hasCash = hasCashState(self)
        self.state = self.Idle
    
    def insertCash(self):
        self.state.insertCash()
    
    def RequestProduct(self):
        self.state.RequestProduct()

    def ejectCash(self):
        self.state.ejectCash()

    def setState(self, state):
        self.state = state

    def getIdleState(self):
        return self.Idle

    def gethasCashState(self):
        return self.hasCash
        

class IdleState(IVendingMachine):

    def __init__(self, state):
        self.state = state

    def insertCash(self):
        self.state.setState(self.state.gethasCashState())
        print("Your Cash is recieved!, please place you order")
    
    def RequestProduct(self):
        print("Insert the Cash First")

    def ejectCash(self):
        print("Cash First, ask for eject then!")

class hasCashState(IVendingMachine):

    def __init__(self, state):
        self.state = state

    def insertCash(self):
        print("You have already inserted the cash, collect/select the order!")
    
    def RequestProduct(self):
        print("Here is your Product")
        self.state.setState(self.state.getIdleState())

    def ejectCash(self):
        self.state.setState(self.state.getIdleState())
        print("Ejected your cash, collect it now!")

if __name__ == "__main__":
    currState = VendingMachine()
    currState.RequestProduct()
    currState.insertCash()
    currState.RequestProduct()
    currState.ejectCash()


# Implement the 'Undo/Redo As a Pattern' using either State Pattern or other design Pattern