# coding=utf-8
# https://projecteuler.net/problem=21
# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
# amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# Completed
# Answer: 31626

n = 220
def properDivisors(n):
    numberList = []
    for x in range(1,n,1):
        if n % x == 0:
            numberList.append(x)
    return sum(numberList)

maxNumber = 10000
total = 0
numbersStr = ''

for x in range(1, maxNumber+1, 1):
    divisorsSum1 = properDivisors(x)
    divisorsSum2 = properDivisors(divisorsSum1)
    if x == divisorsSum2 and (divisorsSum1 != divisorsSum2) and (str(divisorsSum1) not in numbersStr):
        print('{} + {}'.format(divisorsSum1, divisorsSum2))
        numbersStr = numbersStr + "{} {} ".format(divisorsSum1, divisorsSum2)
        total = total + divisorsSum1 + divisorsSum2

print(total)
print(numbersStr)
