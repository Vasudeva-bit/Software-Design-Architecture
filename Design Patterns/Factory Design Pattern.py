from abc import ABCMeta, abstractstaticmethod
# Factory class is encouraged to be singleton to avoid loading or creating the factory class everytime i.e., create new instance.
class ISubject(metaclass=ABCMeta):
    @abstractstaticmethod
    def subject(self):
        """Interface method, to be implemented by subclasses"""

class Math(ISubject):
    def __init__(self):
        self.sub = "Math"

    def subject(self):
        print("Subject is Math")

class CS(ISubject):
    def __init__(self):
        self.sub = "CS"
    
    def subject(self):
        print("Subject is CS")

class SubFactory:

    @staticmethod
    def Creator(choice):
        if(choice == "Math"):
            return Math()
        elif(choice == "CS"):
            return CS()
        print("Invalid")
        return -1



if (__name__ == "__main__"):
    choice = input("Enter the object of the subclass to be created: ")
    sub = SubFactory.Creator(choice)
    if(sub != -1):
        sub.subject()
# used with the integration of SOLID principles