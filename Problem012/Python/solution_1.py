#!/usr/bin/env python
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

# Highly divisible triangular number
# Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number
# to have over five hundred divisors?

from itertools import combinations, count
from functools import reduce


def trianglenums():
    for n in count(start=1, step=1):
        yield n * (n + 1) // 2


def factoring(n):
    divs = [1]
    i = 2
    while n > 1:
        while not n % i:
            n /= i
            divs.append(i)
        i += 1
    return divs


def divisors(n):
    divs = factoring(n)
    primes = divs[1:]

    for j in range(1, len(primes)):
        for comb in combinations(primes, j + 1):
            newdiv = reduce(lambda x, y: x*y, comb)
            if newdiv <= n and newdiv not in divs:
                divs.append(newdiv)
    return len(divs)


# external thing whose I found on thread of that problem
# resuming all (one line! D:) FDP! (divisors + factoring function).
# The perfomance it's the same
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n ** 0.5) + 1) if not n % i))) 


for i in trianglenums():
    if divisors(i) > 500:
        print(i)
        break
