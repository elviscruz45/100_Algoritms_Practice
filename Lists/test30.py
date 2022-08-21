from typing import Counter


test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]


def lista(n,b):
    return [x for x,y in Counter(n).items() if y>b]
        
        
print(lista(test_list,2))