file = open('file.txt', 'r')
f = file.readlines()

newList = []
# print(f)
for line in f:
    if line [-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append()
print(newList)