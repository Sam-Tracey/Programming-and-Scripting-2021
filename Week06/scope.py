# more functions work
# variable scope
# Author: Sam Tracey

var = 10                                            # This is a global variable


def cube(num):
    
    var = 66                                        # This is a local variable (local to the function)     
    print ("In function var is: ", var)                           
    return num ** 3                     
                           
cube(21)
print ("Outside the function var is: ", var) 
print (var)                             