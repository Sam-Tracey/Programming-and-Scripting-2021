# messing with dictionaries during lecture
# Author: Sam Tracey

car = {
    "make": "Ford",
    "price": 123,
    "owner": {
        "first name": "Sam",
        "age": 44
    }
}
print(type(car))
print (car)


car ["model"] = "Focus"
print (car)
#make = car["make"]
#notMake = car.get("aakakakakka")
#print (type(notMake))
#print (make)
print(car["owner"]["age"])