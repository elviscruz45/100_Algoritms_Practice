def par(n):
    return list(filter(lambda x:x%2==0,n))

print(par([12, 14, 95, 3]))

list1 = [2, 7, 5, 64, 14,100,111]
even_list=[i for i in list1 if i%2==0]

print(even_list)