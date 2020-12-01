class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

# print(Dog.num_dogs()) #classmethod

    @staticmethod
    def bark(n):
        """bark n times"""
        for _ in range(n):
            print("Bark!")

Dog.bark(10)