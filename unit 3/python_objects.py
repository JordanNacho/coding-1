# Python objects are digital representations of things
# that can be interact with one another

# objects are collections of data that we use to
# characterize things

# example- a car is a object/ "thing"
# characteristics of a car: engine, tires, battery, seats.
# color, model, doors

# when we want to make an object, we need to use a class
# keyword = object maker

# the class name ALWAYS is capitalized / pascel case

class Car:
    def _init__(self, color, model, doors, engine, tires):
    # attributes are the characteristics of the object
        self.color = color
        self.model = model
        self.doors = doors
        self.engine = engine
        self.tires = tires
        self.battery = "12V"


    # method is a function that is associated with an object