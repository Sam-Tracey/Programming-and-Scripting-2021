# Store a student name and the list of her courses in a dictionaty. Number of courses could change.
# Author: Sam Tracey

student = {"Student Name": "Laura",                 # define student as a dictionary
            "Classes": [                            # Classes defined as an array of dictionary elements as the number of courses could change
                {
                "courseName": "Programming",
                "grade": 45
                },

                {"courseName": "History",
                "grade": 99
                }
            ]
}  

print ("Student:", student["Student Name"])
for count in student["Classes"]:                                    # loop through the student dict to print out each class value
    print("\t", (count["courseName"]),":", "\t", (count["grade"]))      # ensure formatting matches lab sheet. (I still can't get the hang of the {} .format method!)