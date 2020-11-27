class Cat(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am", self.name, "and I am ", self.age, "years old")

    def change_age(self, age):
        self.age = age

said = Cat('Said', 23)
john = Cat('john', 39)
said.change_age(22)
said.speak()
john.speak()
print(said.name)