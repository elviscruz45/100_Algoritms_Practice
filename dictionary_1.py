
from binascii import a2b_base64


key_value={}

key_value[2] = 56       
key_value[1] = 2
key_value[4] = 12
key_value[5] = 24
key_value[6] = 18
key_value[3] = 323

def sorts(key):
    a=key.items()
    b=sorted(a)
    print(a)

print(dict(sorted(key_value.items(),key=lambda x:x[1])))