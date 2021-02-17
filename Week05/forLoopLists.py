# using for loops with lists durng week 04 lecture
# Author: Sam Tracey

list = [2, 4, 5, 6]
more = list + [2,5,6]

for x in more:
    print("element in list: ", x)


for key in range(0,len(more)):
    print ("more[",key, "] = ", more[key])

#print(more)