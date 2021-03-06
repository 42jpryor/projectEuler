# coding=utf-8
# https://projecteuler.net/problem=12
# Highly divisible triangular number

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

# Completed
# Answer: 76576500

# Generate triangle number
counter = 1
triangleNumber = 0
finished = False
while finished == False:
    triangleNumber += counter
    counter += 1
    numberList = []
    # Find the factors for the natural number
    print(triangleNumber)
    for x in range(1,(int(triangleNumber**0.5))+1): # Use square root whenever dealing with factors it's way faster
        if triangleNumber % x == 0:
            numberList.append(x)
        if x > triangleNumber:
            break
    if(len(numberList) >= 250):
        finished = True
        break

print(numberList)
print(triangleNumber)