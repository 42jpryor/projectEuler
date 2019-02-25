# coding=utf-8
# https://projecteuler.net/problem=17
# Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
# ers used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be 
# used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in 
# compliance with British usage.

# Completed
# Answer: 21124

singles = ['',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

tenths = ['','',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

maxNum = 9
totalLength = 0
numberList = []


for x in range(1,1001):
    numberList = map(int,list(str(x)))
    word = ''
    if(len(numberList) == 3):
        word = word + singles[numberList[0]] + 'hundred'
        if numberList[1] > 0 or numberList[2] > 0:
            word = word + 'and'
        del numberList[0]
    if(len(numberList) == 2):
        if numberList[0] == 0:
            del numberList[0]
        elif numberList[0] > 1:
            word = word + tenths[numberList[0]]
            del numberList[0]
        elif numberList[0] == 1:
            del numberList[0]
            word = word + teens[numberList[0]]
            del numberList[0]
    if(len(numberList) == 1):
        word = word + singles[numberList[0]]
        del numberList[0]
    print(word)
    totalLength += len(word)
print(totalLength + 11) # Plus 11 for 1,000