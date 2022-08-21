from audioop import reverse


def max2(n):
    n.sort()
    a=n[-2:-1]
    return a

print(max2([70, 11, 20, 4, 100]))