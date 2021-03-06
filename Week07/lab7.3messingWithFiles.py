# A function that will store a Dict to a file as JSON (JavaScript Object Notation)
# Author: Sam Tracey

import json

filename = "testdict.json"
sample = dict(name="Fred", age=31, grades = [1,34,55])

def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj, f)


writeDict(sample)