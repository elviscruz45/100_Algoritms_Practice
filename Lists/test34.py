test=[1,2,3]

for i in test:
    for j in test:
        for k in test:
            if(i!=j and j!=k and i!=k):
                print(i,j,k)