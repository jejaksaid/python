class Cat(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1,2,3]

    def speak(self):
        print("Hi I am", self.name, "and I am ", self.age, "years old")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

said = Cat('Said', 23)
john = Cat('john', 39)
said.add_weight(60)
john.add_weight(50)
said.change_age(22)
said.speak()
john.speak()
print(john.weight)