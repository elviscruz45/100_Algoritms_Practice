# Python RegEx
#findall, Return a list containing all matches
#Search , Return a Match Object, if tehre is a match anywhere in the string
#split, Return a list where the string has been split at each match
#sub, Replaces one or many matches with a string

import re

comentario1="el precio de 123 este producto es 15 soles"
comentario2="esta huevada, cuesta 25 soles, no me parece justo"

com2=re.findall(" \d\d ",comentario1)

print(com2)

