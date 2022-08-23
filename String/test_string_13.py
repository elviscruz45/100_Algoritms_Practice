import re
str = "Course location is London or Paris!"
mo = re.search(r"location.*[London|Paris|Zurich|Strasbourg]",str)

print(mo.group())

