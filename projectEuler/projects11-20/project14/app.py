# coding=utf-8
# https://projecteuler.net/problem=14
# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Completed
# Answer: 837799

def even(n):
    return n/2

def odd(n):
    return 3 * n + 1


longestLength = 0
number = 0
for x in range(999999,1,-1):
    total = x
    length = 0
    while total > 1:
        length +=1
        if(total % 2 == 0):
            total = even(total)
        else:
            total = odd(total)
    if length > longestLength:
        longestLength = length
        number = x
        print(longestLength)
        print(number)

print("Longest Length: {}".format(longestLength))
print("Number: {}".format(number))