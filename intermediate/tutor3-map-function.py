# map function
li = [1,2,3,4,5,6,7,8]

def func(x):
    return func(x**x)

# print (list(map, func, li))
print([func(x) for x in li if x%2==0])