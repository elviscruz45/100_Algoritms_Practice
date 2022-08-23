
string="GeeksForGeeks"



def removes(string,ith):
    new_str=""
    new_str=string[:ith]+string[ith+1:]
    return new_str

print(removes(string,2))