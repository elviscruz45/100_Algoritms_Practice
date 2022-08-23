text1="khokho"

text2="amaama"

def whatis(text):
    a=text[::-1]
    b=text[:len(text)//2]
    c=text[len(text)//2:]
    if text==a:
        print("It is palindrome")
    if b==c:
        print("It is symetrical")
    print("--------"+text)
        
whatis(text1)
whatis(text2)