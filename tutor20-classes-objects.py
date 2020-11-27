x = 'string'
y = 22
boo = True
# object
# print(type(y))
# print(x.strip('1'))
# print(x.count('1'))
# print(boo.count('1')) its wrong
# print(x.count())
#
# def func():
#     print('hello')
# func()

# class
class number():
    def __init__(self, num):
        self.var = num

    def display(self, x):
        print(x)

num = number(22)
num.display(num.var)