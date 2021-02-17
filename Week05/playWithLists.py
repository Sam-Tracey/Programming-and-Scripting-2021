# week 4 lecture and subsequent list manipulation
# Author: Sam Tracey

list = [2, 3, 4]
print(list)
print(type(list))
print(len (list))
list.append(99)
print(list)

biggerlist= list + [10, 11, 12]
print(biggerlist)
print(len(biggerlist))

aList = [2, 3.5, True, "Hi Sam", [1, 3], {}]
print(aList)
print(len(aList))


print(aList[0])                 # first element in list
print(aList[4])                 # fifth element in list
print(aList[-6])                # last element in list
aList [5] = 9999                # assigning a value to the 6th element
print(aList)
print(aList [1:4])              # print out from 2nd to 4th element in list
print(aList[1:])                # print out from second element to end of list
print(aList [:4])               # print out each element in list up to the 3rd element
print(aList[::2])               # print every other element in list starting from 0
print(aList[::-1])              # print list in reverse

x = aList.pop(0)                # assigning the first element from aList to variable x and remove it from list
print(aList) 
print(x)