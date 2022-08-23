
def remove(string,ith):
    string=list(string)
    del string[ith-1]
    string="".join(string)
    return string


string="GeeksForGeeks"



def removes(string,ith):
    new_str=""
    for i in range(len(string)):
        if i!=ith:
            new_str+=string[i]
    return new_str

print (removes(string,2))
