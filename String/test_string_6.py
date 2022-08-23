# Python RegEx
#findall, Return a list containing all matches
#Search , Return a Match Object, if tehre is a match anywhere in the string
#split, Return a list where the string has been split at each match
#sub, Replaces one or many matches with a string

import re

txt = "The rain in Spain"

x = re.findall("[A-h]", txt)
print(x)

