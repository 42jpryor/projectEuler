# coding=utf-8
# https://projecteuler.net/problem=22
# Names Scores

# Completed
# Answer: 871198282
from names import *
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
strings = list(firstNames)
def letterScore(n):
    return alphabet.find(n.upper()) + 1

print('Length of List: {}'.format(len(strings)))
strings.sort()

total = 0

for x in range(0,len(strings), 1):
    wordTotal = 0
    stringList = list(strings[x])
    for y in stringList:
        wordTotal += letterScore(y)
    print(total)
    total = total + (wordTotal * (x+1))

print(total)



