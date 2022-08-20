# you can put in as many parameters as you want. 
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print (add(3, 4, 5, 6, 7))

# *kwargs is treated as a dictionary in type. 
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
