from abc import ABCMeta, abstractstaticmethod

class ISubject(metaclass=ABCMeta):

    @abstractstaticmethod
    def printsubject():
        """This is a abstract method, to be implemented in subclass"""

class SubjectSingleton(ISubject):

    __instance = None # keeping the variable '__instance' is key to
    # implement singleton using python i.e., the __instance is examined
    # any time a object is created in __init__

    @staticmethod
    def get_instance():
        if(SubjectSingleton.__instance is None):
            SubjectSingleton("Defualt Name", 0)
        return SubjectSingleton.__instance
        

    def __init__(self, sub, marks):
        if SubjectSingleton.__instance is None:
            SubjectSingleton.__instance = self
            self.sub = sub
            self.marks = marks
        else:
            raise Exception("Singleton Design: An instance is already created!")
    
    @staticmethod
    def printsubject():
        print(f"{SubjectSingleton.__instance.sub}: {SubjectSingleton.__instance.marks}")


obj = SubjectSingleton("CS", 99)
print(obj)
obj.printsubject()
obj = SubjectSingleton("Math", 98) # Raises an exception as already the __instance is not None
print(obj)
obj.printsubject()