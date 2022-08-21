def count(n):
    even=len(list(filter(lambda x:x%2==0, n)))
    odd=len(list(filter(lambda x:x%2!=0,n)))
    return even, odd


print(count([12, 14, 95, 3]))