# coding=utf-8
# https://projecteuler.net/problem=20
# Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# Completed
# Answer: 648

n = 100
total = 1
for x in range(n,1,-1):
    total = total * x

totalStr = map(int,list(str(total)))

print(sum(totalStr))

