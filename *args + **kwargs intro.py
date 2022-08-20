# you can put in as many parameters as you want. 
# args has has a data type of tuple
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print (add(3, 4, 5, 6, 7))

# *kwargs has data typee dictionary. 
# it takes in positional parameters. 
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

class Car:

    def __init__(self, **kw):
        # using the get() function, we can get hold of the value
        # when using get(), if the key is not in the dictionary, it will just return none
        # this is important because we can initialise them like this as well:
        # self.make = kw["make"]
        # self.make = kw["model]
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Toyota")
# if I did not use the get() function and asked the computer to print "my_car.model" without specifying
# then the computer would return an error.
# the get() function allows us the privilege of not having to specify an aforementioned parameter. 
print(my_car.model)
