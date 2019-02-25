# coding=utf-8
# https://projecteuler.net/problem=16
# Lattice paths

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# Completed
# Answer: 1366

total = 2**1000
numberList = map(int,list(str(total)))

print(sum(numberList))
