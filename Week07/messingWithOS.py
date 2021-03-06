# Messing with OS. See if a file exists

import os

filename = 'amIHere.txt'


if (os.path.exists(filename)):
    print("file exists")
else:
    with open(filename, "x") as f:
        print("Creating the file")