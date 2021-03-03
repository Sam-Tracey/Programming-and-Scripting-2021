# Programming and scripting Lab 6. Functions.
# Author: Sam Tracey



def menu():                                                     # Function to display menu
    print("What would you like to do?")
    print("\t (a) Add new students")
    print("\t (v) View students")
    print ("\t Quit")
    choice = input("Type on letter (a/v/q):")
    return choice


students = []
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["Name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module) 
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules
    

def doAdd(students):
    currentStudent={}
    currentStudent["Name"] = input("Enter name: ")
    currentStudent["Modules"] = readModules()
    students.append(currentStudent)


def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["Name"], module["grade"]))


def doView(students):
    for currentStudent in students:
        print(currentStudent["Name"])
        displayModules(currentStudent["Modules"])




# Start of main program
students = []
choice = menu()
while choice != "q":
    if choice == "a":
        doAdd(students) 
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\n Please select (a,v or q)")
    choice = menu()
       
