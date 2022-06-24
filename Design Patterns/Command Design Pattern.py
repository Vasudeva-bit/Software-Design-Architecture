from abc import ABCMeta, abstractstaticmethod

class ICommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute():
        pass
    @abstractstaticmethod
    def undo():
        pass


class IDevice(metaclass=ABCMeta):
    @abstractstaticmethod
    def On():
        pass
    
    def Off():
        pass

    def Up():
        pass

    def Down():
        pass

class TV(IDevice):
    def On(self):
        print("Device is On")

    def Off(self):
        print("Device is OFF")

    def Up(self):
        print("Volume is Up")

    def Down(self):
        print("Volume is Down")

class OnC(ICommand):
    def __init__(self, command):
        self._command = command

    def execute(self):
        self._command.On()

    def undo(self):
        self._command.Off()

class OffC(ICommand):
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.Off()

    def undo(self):
        self.command.On()

class UpC(ICommand):
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.Up()

    def undo(self):
        self.command.Down()

class Button:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()

    def unpress(self):
        self.command.undo()

if __name__ == "__main__":
    reciver = TV()
    command = OnC(reciver)
    press = Button(command)
    press.press()

    command = OffC(reciver)
    press = Button(command)
    press.press()

    command = UpC(reciver)
    press = Button(command)
    press.press()
    press.unpress()
    press.unpress()
