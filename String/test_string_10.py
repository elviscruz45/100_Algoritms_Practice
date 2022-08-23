import re

txt = "The rain in Spain"
x = re.search(r"\br\w+", txt)
print(x.group())

