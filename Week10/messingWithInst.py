# week 10 tutorial work along messing with inst (classes)
# Author: Sam Tracey

class Nameofclass:
    name = ''
    last = ''
    def getfullname(self):
        return self.name + ' ' + self.last

    


inst = Nameofclass()
inst2 = Nameofclass()


inst.name = 'Sam'
inst2.last = 'Tracey'

person = inst
print (person.name)

inst.last = 'Tracey'
print (person.getfullname())


string1 = 'Blah blah'
string2 = string1
string1 += 'With bells on'

print (string2)