def sum(n):
    num=0
    avr=0
    for i in n:
        num+=i
        avr+=i/len(n)
    return num,avr

print(sum([15, 9, 55, 41, 35, 20, 62, 49]))

#--------------------------------------------------------------------------------------------------------
