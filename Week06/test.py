students = []


def readModules():
    return[]


def doAdd(students):
    currentStudent = {}
    currentStudent["Name"] = input("Enter name: ")
    currentStudent["Modules"] = readModules()

    students.append(currentStudent)

doAdd(students)

doAdd(students)
print (students)