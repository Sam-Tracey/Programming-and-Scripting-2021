# This program takes in a positive floating-point number and outputs an approximation of its square root.
# The object is to define our own fucntion for calculating the square root and not to use one of the built-in functions.
# Author: Sam Tracey

def sqrt(num, error= 0.0000001):
    estimate = num
    diff = 9999999999                                                       # arbritary large value for the variable diff (difference) this will get much smaller as we iterate through the loop
    while diff > error:                                                     # keep looping while the variable diff is greater than the error value stipulated in arg 2 of the function.
        
        # Based on Newton's method formula (found at https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html )
        newEstimate = estimate - ((estimate**2 - num) / (2*estimate))

        # There is a potential for a negative value here so use ABS to ensure diff remains positive
        diff = abs(newEstimate - estimate)
        estimate = newEstimate
    return estimate

userNumber = float(input("Please enter a positive number: "))               # Assign value entered by user as variable userNumber
while userNumber < 0:                                                       # Error checking - ensure number entered is positive.
    userNumber = float(input("Please enter a positive number: "))

rootNumber = sqrt(userNumber)
print("The sqaure root of {} is approximately {}".format(userNumber, rootNumber))
