"""MVC: Separation of Concers Principle. Always used where ever there is a User Interface or interaction"""
class View:
    """View is responsible to just deliver the output rendered based on the request"""
    def __init__(self):
        """No need to implement Constructor"""
    def response(self, val):
        print("The response from the Model is ", val)

class Controller:
    """Controller is repsonsible for accepting the request, passing the request to Model, pass response from
    Model to View to request the render view for response"""
    def __init__(self):
        self.view = View()
        self.Model = Model()

    def response(self, val, operation):
        self.request_model(val, operation)

    def request_model(self, val, operation):
        self.request_view(self.Model.response(val, operation))

    def request_view(self, val):
        self.view.response(val)

class Model:
    """Model is responsible for accepting the request from Controller, process the request and generate the response"""
    def __init__(self):
        """No need to implement Constructor"""

    def response(self, val, operation):
        if operation == 'square':
            return val**2
        
        elif operation == 'cube':
            return val**3

        else:
            return "Enter Valid Operation [Square, Cube]"

"""Main Idea of the MVC pattern is to decouple the interactions between the Model and View directly.
MVC is mostly used in building web apps so the model and view are separated through controller"""

if __name__ == "__main__":
    controller = Controller()
    controller.response(2, 'square')
