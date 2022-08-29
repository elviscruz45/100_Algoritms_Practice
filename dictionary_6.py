def dictionary(input):
    a=0
    for i,v in input.items():
        a+=v
    return a
        
print(dictionary({"x": 25, "y":18, "z":45}))