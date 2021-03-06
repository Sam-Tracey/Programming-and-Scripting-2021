# Coding along with Andrew Beatty
# Author: Sam Tracey 

with open(".\lecture.txt", "w") as f:
    print ("create a file")


with open("testData.txt", "rt") as f:       # only reads from current directory
    # data = f.read()                       # you can stipulate the number of characters to read in bracket
    # print (data)
    for line in f:                          # iterate through lines in txt file
        print("we got: ", line.strip())     # .strip removes carriage returns etc.

with open("output.txt", "at") as f:         # "at" appends to the file without overwriting
# with open("output.txt", "wt") as f:
    f.write("Hello mum \n test")            # 3 different methods of writing to a file one with f.write the other with print.
    print(" my data", file= f)              # this method appends to a current txt file, the above OVERWRITES data in the txt file because of "wt"