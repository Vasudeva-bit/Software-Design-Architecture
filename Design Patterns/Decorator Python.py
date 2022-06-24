def mydecorator(to_be_decorated):
    def wrapper(*args, **kwargs):
        print("Decoration in Progress!")
        return to_be_decorated(*args, **kwargs)
    return wrapper

@mydecorator
def printer(name):
    return f"Hello, {name}"

print(printer("Vasudeva"))

# Practical Examples of Decorators in Python
# 1. timer for any function execution
# 2. logging into a site

# Timer Example
