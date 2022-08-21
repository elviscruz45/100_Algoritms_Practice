def even(a,b):
    if a>=b:
        return
    if a&1:
       a=a+1 
    print(a)
    return even(a+2,b)

even(1,15)