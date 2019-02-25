# coding=utf-8
# https://projecteuler.net/problem=6
# Sum Square difference
# The sum of the squares of the first ten natural numbers is,
#                                   12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#                                   (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Completed
# Answer: 25164150

tot1 = 0
tot2 = 0
total = 0
for x in range(1,101):
    tot1 = tot1 + (x * x)
    tot2 += x

tot2 = tot2 * tot2
total = tot2 - tot1

print(total)
