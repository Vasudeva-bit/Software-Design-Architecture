"""
Adapter Design Pattern
"""
from abc import ABCMeta, abstractstaticmethod
class IMath(metaclass=ABCMeta):
    @abstractstaticmethod
    def subject_math():
        """This is just a abstract method for math"""

class Math(IMath):
    def subject_math(self):
        print("Subject: Math")

class ICS(metaclass=ABCMeta):
    @abstractstaticmethod
    def subject_CS():
        """This is just a abstract method for CS"""

class CS(ICS):
    def subject_CS(self):
        print("Subject: CompSci")

class CS_Adapter(IMath):
    def __init__(self):
        self.CS = CS()
    def subject_math(self):
        self.CS.subject_CS()

if __name__ == "__main__":
    obj = Math()
    obj.subject_math()
    # obj = CS() * raises a AttributeError "CS" object has no attribute *
    obj = CS_Adapter()
    obj.subject_math()