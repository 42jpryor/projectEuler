# coding=utf-8
# https://projecteuler.net/problem=7
# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

# Completed
# Answer: 104713

currentNum = 2
primes = []
z = False
while True:
    for x in range(2,currentNum+1):
        if(x == currentNum):
            primes.append(currentNum)
            print(currentNum)
        if(currentNum % x == 0):
            break
    currentNum+=1
    if(len(primes) == 10001):
        break
