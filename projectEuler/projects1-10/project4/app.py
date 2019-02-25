# coding=utf-8
# https://projecteuler.net/problem=4
# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Completed
# Answer: 906609

largestX = 0
largestY = 0
largest = 0
total = 0

for x in range(999,100,-1):
    for y in range(999,100,-1):
        total = x * y
        if(str(total) == (str(total)[::-1]) and total > largest):
            largest = total
            print(str(x) + " * " + str(y))
            print(largest)
