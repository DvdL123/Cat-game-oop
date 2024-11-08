# Our Cat Entity
class Cat:
    # The constructor
    # - The constructor will create a cat for us in code
    # - To create a cat, we need a given_name and given_colour

    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour

# An instance of Cat
# An instanc eos a specific occurance of a class
mimi = Cat("Mimi", "Brown")
print(mimi.name)
print(mimi.colour)
