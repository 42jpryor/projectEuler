# coding=utf-8
# https://projecteuler.net/problem=18
# Maximum path sum 1

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, 
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, 
# and requires a clever method! ;o)

# Instead of adding each combination of numbers each time, instead just subtract and then add the next number that is needed

import time

numberList = [[7],[95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

# 3
# 7 4
# 2 4 6
# 8 5 9 3

numberList1 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

largestSum = 0

total1 = numberList1[0][0] + numberList1[1][0] + numberList1[2][0] + numberList1[3][0]
total2 = numberList1[0][0] + numberList1[1][0] + numberList1[2][0] + numberList1[3][1]


total3 = numberList1[0][0] + numberList1[1][0] + numberList1[2][1] + numberList1[3][1]
total4 = numberList1[0][0] + numberList1[1][0] + numberList1[2][1] + numberList1[3][2]


total5 = numberList1[0][0] + numberList1[1][1] + numberList1[2][1] + numberList1[3][1]
total6 = numberList1[0][0] + numberList1[1][1] + numberList1[2][1] + numberList1[3][2]

total7 = numberList1[0][0] + numberList1[1][1] + numberList1[2][2] + numberList1[3][2]
total8 = numberList1[0][0] + numberList1[1][1] + numberList1[2][2] + numberList1[3][3]

print('{} {} {} {} {} {} {} {}'.format(total1, total2, total3, total4, total5, total6, total7, total8))



start = time.time()
total = 0
total = total + numberList1[0][0]
for z in range(2):
    total = total + numberList1[1][z]
    for y in range(2):
        total = total + numberList1[2][y+z]
        for x in range(2):
            total = total + numberList1[3][x+y+z]
            if total > largestSum:
                largestSum = total

            total = total - numberList1[3][x+y+z]
        total = total - numberList1[2][y+z]
    total = total - numberList1[1][z]


print(largestSum)

end = time.time()
print(end - start)


