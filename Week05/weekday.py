# This program output whether the current day is a week day or not.
# Author: Sam Tracey

from datetime import date

today = date.today()
weekDay = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")


if today in weekDay:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")

