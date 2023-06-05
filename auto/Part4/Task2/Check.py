from HashDict import HashDict
from random import randint

hashDict = HashDict()
pyDict = {}

for i in range(100):
    key = randint(1, 1000)
    value = randint(1, 1000)
    hashDict[key] = value
    pyDict[key] = value

for key in pyDict.keys():
    assert hashDict[key] == pyDict[key]