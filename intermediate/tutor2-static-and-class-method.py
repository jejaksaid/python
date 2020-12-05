# static and class method
class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.populationd

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = person('said', 18)

print(person.isAdult(21))