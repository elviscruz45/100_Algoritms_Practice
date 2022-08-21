test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

def dic(n):
    new={}
    for i in test_list:
        new[(i[0],i[1])]=(i[2],i[3])
    return new



#--------------------------------------------------------------------------------------------------------

news={tuple(i[:2]):tuple(i[2:]) for i in test_list}
print(news)