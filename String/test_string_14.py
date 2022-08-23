
def remove(string,ith):
    string=list(string)
    del string[ith-1]
    string="".join(string)
    return string


string="GeeksForGeeks"

print (remove(string,3))