# still messing with functions
# Anonymous functions
# Author: Sam Tracey



def tripler(num):
    return num * 3

isMax = True
if isMax:
    fun = lambda num : num * 2                  # anaonymous function as it doesn't have a name like triple. Takes in 1 variable and returns 1 variable
else:
    fun = tripler



var = fun(10)
print (var)



