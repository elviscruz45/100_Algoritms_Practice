lista1=[4, 5, 5, 5, 3, 8]

1, 22

def func(n):
    new=[]
    for i in n:
        if lista1.count(i)==3 and i not in new:
            new.append(i)
    return new

print(func(lista1))