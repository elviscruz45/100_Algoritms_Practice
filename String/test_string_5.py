def primos(num):
    numbers=[i for i in range(3,num+1)]
    primos=[1,2]
    for i in numbers:
        n=2
        prim=True
        while n<i:
            if i%n==0:
                prim=False
            n+=1
        if prim==True:
            primos.append(i)
    return primos

print(primos(100))