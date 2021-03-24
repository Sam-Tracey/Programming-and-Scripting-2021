# Messing with Init work along
# Author: Sam Tracey


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def fullname(self):
        if hasattr(self, 'middlename'):
            return self.firstname + ' ' + self.middlename + ' ' + self.lastname
        return self.firstname + ' ' + self.lastname
    def __str__(self):
        return self.fullname()
    def addmiddlename(self, middlename):
        self.middlename = middlename


person1 = Person('Sam', 'Tracey')
person1.addmiddlename ('James')
print (person1.firstname)
print (person1.fullname())
print(person1)