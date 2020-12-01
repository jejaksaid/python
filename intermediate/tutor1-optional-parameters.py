# optional parameters
# 1 example
def func(x):
    return x **2

call = func(5)
print(call)

# 2
def func(x=1):
    return  x **2

call = func(4) # if you put a number to this section, this will override the def function which is x=1
print(call)

# 3
def func(word, freq=1):
    print(word*freq)

# call = func('said', 10)
call = func(100)

# 4 multiple params
def func(word, add=5, freq=2):
    print(word*(add-freq))

call = func('hi', 40, 1)

# 5 more complex
class car(object):
    def __init__(self, make, model, year, condition='Second', kms=100):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s." %(self.make, self.model, self.year))
whip = car('BMW', 'Fusion', 2012, 'New', 0)
whip.display(True)













