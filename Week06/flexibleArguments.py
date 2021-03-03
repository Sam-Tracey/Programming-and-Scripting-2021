# More messing about with functions.
# Flexible arguments
# Author: Sam Tracey


print ("Hi", 55, 34, [], {}, sep=":")                   # Illustrating multiple arguments for a Python function


# flexible number of arguments

def average(*numbers):
    sumOf = sum(numbers)
    return sumOf / len(numbers)

ave = average(12,11,14,10,9,1,8)                        # passing in multiple arguments to the function average
print("Average is: ", ave)

# flexible number of named arguments

def fun(arg1 = 0, arg2 = 1):                            # stipulating default values if arguments are not passed into the function fun
    return arg1 - arg2


print(fun(6, 10))                                       # returns -1 if no arguments are passed when calling fun function

def funckyArgs(**args):                                 # ** allows you to pas in a variable number of named arguments tinto a function
    print(args)

funckyArgs(name = "Joe", Age = 33, courses = [])        # passing multiple arguments into funckyArgs and they are stored in a dict object