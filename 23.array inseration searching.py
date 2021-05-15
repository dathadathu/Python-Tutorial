#creation of array empty
"""
import array as arr
a = arr.array('i',[])

s = int(input('Enter the length of the array: '))

for i in range(s):
    x = int(input('Enter the value:'))
    a.append(x)

print(a)

val = int(input('Enter the value for search: '))

k= 0
for e in a:
    if e == val:
        print(k)
        break

    k += 1

print(a.index(val))

"""

from array import *

a = array('i',[])

s = int(input('Enter the length of the array: '))

for i in range(s):
    x = int(input('Enter the value:'))
    a.append(x)

print(a)

del a[2]

print(a)

a.remove(6)
print(a)
a.pop(4)
print(a)

print(a[::-1])