# Store the months of a year in a tuple and then create a second tuple from that which contains the summer months.
# Author: Sam Tracey


monthsOfYear = ("January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December")

summer = monthsOfYear[4:7]
for month in summer:
    print (month)