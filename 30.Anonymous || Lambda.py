def sq(n):
    return n*n

print(sq(5))

f = lambda a : a * a
f(25)

#filter map reduce
"""
def is_even(n):
    return n%2 == 0
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11]

evens = list(filter(lambda n : n%2 == 0, nums))

double = list(map(lambda n : n+2 ,evens))

from functools import *
sum = reduce(lambda m, n : m+n, double )
print(evens)
print(double)
print(sum)