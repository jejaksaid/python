class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")

said = Dog('Said', 11)
said.speak()