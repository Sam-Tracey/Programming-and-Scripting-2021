# use person module work along
#Author: Sam Tracey
from personmodule import *

person1 = {
    'firstname': 'Sam',
    'lastname': 'Tracey',
    'dob': dt.date(2010,1,1),
    'height': 180,
    'width': 100
}

displayperson(person1)
gethealthdata(person1)