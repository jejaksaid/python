var = 9
loop = True

# local
# def func(x):
#     newVar = 7
#     print(loop)
#     if x == 5:
#         return newVar
# def otherFunc():
#     newVar = 5
#     print(newVar)
# func(2)

# global
def func(x):
    global loop
    loop = 7

    if x == 5:
        return newVar
def otherFunc():
    newVar = 5

loop = False
# func(2)
print(loop)