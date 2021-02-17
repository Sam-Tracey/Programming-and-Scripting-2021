# generate primes
# Author: Sam Tracey

primes = []
upTo = 10000

for candidate in range (2, upTo):
    # print(candidate)
    isPrime = True
    # only need to check if divisible by prime
    for divisor in primes:
        # if divisable by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break
    if isPrime:
        primes.append(candidate)

print (primes)