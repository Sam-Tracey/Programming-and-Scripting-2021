# Program reads in a students percentage mark and prints out the corresponding grade
# < 40% = fail, 40%-49% = Pass, 50%-59% = Merit 2, 60%-69% = Merit 1, >70% = Distinction
# Author: Sam Tracey

score = float(input("Enter the percentage:"))

if score < 0 or score > 100:                                                    # Error check
    print ("Invalid percentage, please enter a number between 1 and 100")         # Error message output if the value entered is less than 0 or greater than 100
elif round(score) < 40:                                                                # check if value entered meets Fail criteria
    print ("Fail")
elif round(score) < 50:                                                                # check if value entered meet Pass criteria
    print ("Pass")
elif round(score) < 60:                                                                # check if value enterd meets Merit 2 criteria
    print ("Merit 2")
elif round(score) < 70:                                                                # check if value entered meets Merit 1 criteria
    print ("Merit 1")
else:                                                                           # the only criteria available is distinction
    print ("Distinction")
