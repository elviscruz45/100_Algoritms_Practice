def swap(n,a,b):
    n[a-1],n[b-1]=n[b-1],n[a-1]
    return n

print(swap([23, 65, 19, 90],1,3))