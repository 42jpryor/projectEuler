# https://projecteuler.net/problem=5
# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Completed
# Answer: 232792560
# Side Note: This answer took ages to calculate

num = 0
z = False
while z == False:
    num+=1
    print(num)
    for x in range(20,1,-1):
        if(num % x != 0):
            z = False
            break
        else:
            z = True

if(z == True):
    print("Smallest Multiple:" + str(num))