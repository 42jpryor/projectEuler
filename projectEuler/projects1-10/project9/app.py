# coding=utf-8
# https://projecteuler.net/problem=9
# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# 200, 375, 425
# Completed
# Answer: 31875000


for a in range(1001,1,-1):
    for b in range(1001,1,-1):
        for c in range(1001,1,-1):
            sumTot = (float(a)*a) + (b*b)
            if(sumTot / (c) == c):
                total = a + b + c
                if total == 1000:
                    if(a<b and b<c):
                        print("{} + {} = {}").format(a,b,c)
