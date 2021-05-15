def fact(n):
    F = 1
    for i in range(1, n+1):
        F = F * i
    return F
    fact()

#print(fact(5))


#recurrsion
#function calling itself
'''
def greet():
    print("Hello")
    greet()

greet()


#limit of recurrsion

import sys
print(sys.getrecursionlimit())
'''

#using recurrsion
def f(n):

    if n == 0:
        return 1

    return n * f(n-1)

ff = f(5)
print(ff,"ff")