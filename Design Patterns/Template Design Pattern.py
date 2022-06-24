from abc import ABCMeta, abstractstaticmethod

class Student:
    @abstractstaticmethod
    def enroll(self):
        """The function is implemented in the child class"""
    @abstractstaticmethod
    def take_exam(self):
        """The function is implemented in the child class"""

    def join(self):
        self.enroll()
        self.take_exam()

class MathStudent(Student):
    def enroll(self):
        print("You are enrolled in Math Class")

    def take_exam(self):
        print("Take the Math Exam")

class CSStudent(Student):
    def enroll(self):
        print("You are enrolled in CS Class")

    def take_exam(self):
        print("Take the CompSci Exam")

if __name__ == "__main__":
    cs = CSStudent()
    cs.enroll()
    cs.take_exam()
    
    math = MathStudent()
    math.enroll()
    math.take_exam()
