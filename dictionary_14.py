test_tup1 = ('GFG', 'is', 'best')
test_tup2 = (1, 2, 3)

a=zip(test_tup1,test_tup2)


b={x:y for x,y in a}

print(b)