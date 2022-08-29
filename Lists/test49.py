#Python List Exercise
#Python – Swap elements in String list

from importlib.abc import ResourceLoader
from importlib.util import module_from_spec
from socket import setdefaulttimeout


array = [['java', 1995], ['c++', 1983],['python', 1989]]


for i in range(2):
    column = sorted(array, key = lambda x:x[i])
    print(column)

