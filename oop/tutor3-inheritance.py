# class Dog(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age, "years old")
#
#     def talk(self):
#         print('Bark!')
#
# class Cat(Dog): # parents child things
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#
#     def talk(self):
#         print('Meow!')
#
# john = Dog('jogn', 30)
# john.talk()
#
# said = Cat('Said', 11, 'red')
# said.talk()

class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep beep')


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('Honk honk')

