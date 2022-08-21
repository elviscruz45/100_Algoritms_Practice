list1 = [10, 21, 4, 45, 66, 93, 11]

list2 = [12, 14, 95, 3, 73]


def odd(n):
    return list(filter(lambda x:x%2!=0,n))


print(odd(list1))

list3=[i for i in list2 if i%2!=0]

print(list3)