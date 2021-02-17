# messing with while loops
# Author: Sam Tracey


# while condition:
#   statements

count = 0                                               # counter controlled while loop increasing
while count < 10:
    print(count)
    count +=1


count = 10                                              # counter controlled while loop decreasing                                      
while count > 0:
    print(count)
    count -=1
print("Blast off!")


val = input("Enter something (q to quit):")             # sentinel control while loop
while val != 'q':
        print ("You said: " + val)
        val = input("(q to quit):")
print ("Goodbye")