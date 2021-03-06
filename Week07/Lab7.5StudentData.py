# Programming and scripting Lab 7. 
# Author: Sam Tracey

import json

filename = "students.json"
students = []

def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj, f)

def menu():                                                     # Function to display menu
    print("What would you like to do?")
    print("\t (a) Add new students")
    print("\t (v) View students")
    print("\t (s) Save students")
    print("\t (q) Quit")
    choice = input("Type on letter (a/v/s/q):")
    return choice



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


def doSave(students):
    writeDict(students)
    print("students save")




# Start of main program
students = []
choice = menu()
while choice != "q":
    if choice == "a":
        doAdd(students) 
    elif choice == "v":
        doView(students)
    elif choice == "s":
        doSave(students)
    elif choice != "q":
        print("\n Please select (a,v or q)")
    choice = menu()