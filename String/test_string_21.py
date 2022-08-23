#--------Python String Exercise-------
# Python program to print even length words in a string

s = "i am laxmi"

def nuevo(s):

    return " ".join(filter(lambda i: len(i)%2==0,s.split()))

print(nuevo(s))


