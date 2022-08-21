def even(a,b):
    n=[i for i in range(a,b)]
    return list(filter(lambda x:x%2==0 and x>=4 and x<15,n))

print(even(8,11))


#--------------------------------------------------------------------------------------------------------


# Python program to print Even Numbers in given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

#creating even starting range
start = start+1 if start&1 else start


#create a list and printing element
#contains Even numbers in range
[ print( x ) for x in range(start, end + 1, 2)]

