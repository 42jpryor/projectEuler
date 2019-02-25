# https://projecteuler.net/problem=3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143?

# Completed
# Answer: 6857

number = 600851475143
factors = []
remainder = False
inc = 2
while remainder == False:
    if number % inc == 0:
        factors.append(inc)
        number = number / inc
        print(inc)
    else:
        inc+=1

print(factors)