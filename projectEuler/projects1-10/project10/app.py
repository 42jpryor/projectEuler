# coding=utf-8
# https://projecteuler.net/problem=10
# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Completed
# Answer: 142913828922
# Code never finished when I tried doing this, had to look it up

currentNum = 2 # Starting number
primes = []
maxNumber = 2000000

# Had to look up how to do this more efficiently
# A composite number is a positive number greater than 1 that is not prime. 
# Every composite number has a factor less than or equal to its square root.

for possiblePrime in range(2, maxNumber + 1):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        print(possiblePrime)
        primes.append(possiblePrime)


print(sum(primes))
