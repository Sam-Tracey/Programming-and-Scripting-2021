# more messing with dictionaries
# ussing for loops to iterate
# Author: Sam Tracey

car = {
    "make": "Fiat",
    "model": "Punto",
    "price": 10000,
    "tags": ["pre-owned", "best-buy", "dealer"]
}

print(car)


#for key in car:
 #   print(key, "have a value", car[key])

print(car.items())
for key, value in car.items():
    print(key, "has a value", value)
    #print (type(pair))
