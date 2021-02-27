# This program output whether the current day is a week day or not.
# Author: Sam Tracey

from datetime import date                                               # Import datetime from the date modulde

today = date.today()                                                    # assign the current day based on system date to variable today
weekDay = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")      # assign the day corresponding to week days to list weekDay


if today in weekDay:                                                    # determine if the value stored in today is in the list weekDay
    print("Yes, unfortunately today is a weekday")                      # Output if today is in weekDay
else:
    print("It is the weekend, yay!")                                    # Output if today is not in list weekDay

