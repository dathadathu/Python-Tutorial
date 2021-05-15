"""
for i in range(5):
    for j in range(5):
        print("#",end="")

    print()

for i in range(5):
    for j in range(i+1):
        print("#",end="")

    print()

for i in range(5):
    for j in range(5-i):
        print("#",end="")

    print()

for i in range(1,5):
    for j in range(i,5):
        print(j,end="")

    print()
"""

str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])