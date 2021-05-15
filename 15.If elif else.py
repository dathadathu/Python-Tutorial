#conditional statements
'''
x = 4
r = x % 2

if r == 0:
    print("Even")
    if x>5:
        print("Great")
    else:
        print("Not so great")

else:
    print("Odd")
'''
#if elif else
'''
x = 4

if(x == 1):
    print("One")
elif(x == 2):
    print("Two")
elif(x == 3):
    print("Three")
else:
    print("Four")
    
'''
#Exercise 1
n = 0

if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")

#Exercise 2
x = int(input())
y = int(input())
z = int(input())
if x>y and x>z:
    print("X")
elif y>x and y>z:
    print("Y")
else:
    print("Z")