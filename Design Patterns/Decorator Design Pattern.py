from abc import ABCMeta, abstractstaticmethod

class ISubject:
    def applications():
        """To be implemented by the child classes"""

class Math(ISubject):
    def applications(self):
        return "Applications include basic systems such as calculator"

class CS(ISubject):
    def __init__(self):
        self.math = Math()

    def applications(self):
        return self.math.applications().replace("basic", "advanced A.I").replace("calculator", "Self Driving Cars")

if __name__ == "__main__":
    math = Math()
    print(math.applications())

    cs = CS()
    print(cs.applications())