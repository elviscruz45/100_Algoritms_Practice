array = [['java', 1995], ['c++', 1983],['python', 1989]]


for i in range(2):
    column = sorted(array, key = lambda x:x[i])
    print(column)


