# coding=utf-8
# https://projecteuler.net/problem=19
# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Completed
# Answer: 171


# TODO
# Figure out the number of days total
# From Jan 1 1901, Tuesday to Dec 31 2000, Sunday

day = 1
startYear = 1901
endYear = 2000
year = 0
numOfSundays = 0

week = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

months = [
    ['Jan', 31],
    ['Feb', 28],
    ['Mar', 31],
    ['Apr', 30],
    ['May', 31],
    ['Jun', 30],
    ['Jul', 31],
    ['Aug', 31],
    ['Sep', 30],
    ['Oct', 31],
    ['Nov', 30],
    ['Dec', 31]
]

for x in range(startYear, endYear + 1, 1): # Loops through years
    if x % 4 == 0:
        months[1][1] = 29
    else:
        months[1][1] = 28
    for y in range(0,len(months)): # Loops through months
        for z in range(1, months[y][1] + 1): # Loops through days
            day+=1
            if day % 7 == 0:
                day = 0
                if z == 1:
                    numOfSundays += 1
            print('{}/{}/{}'.format(y + 1,z,x))

print(day)
print(numOfSundays)

