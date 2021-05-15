'''
Av = 10

x = int(input("How many candies you want?"))

i = 1
while i <= x:
    if i >= Av:
        print("Out of Stock")
        break

    print("Candies")
    i +=1

print("Bye")

for i in range(1,101):
    if i%3 != 0 and i%5 != 0:
        continue
        print(i)

for i in range(1,51):

    if(i%2 != 0):
        pass
    else:
        print(i)

pn = int(input("Number please"))
for i in range(2,pn):
    if (pn%i) == 0:
        print(pn,"Not prime")
        break
    else:
        print(pn,"prime")

n = int(input("Number"))
F = 1
if n<0:
    print("Not a Factorial Number")
elif n == 0:
    print("0 factorial is 1")
else:
    for i in range(1,n+1):
        F = F*i
        print("The factorial of",n," ",F)


'''
n = 5
count = 0
n1,n2 =0,1
while count < n:
    print(n1)
    nt = n1 + n2
    n1 = n2
    n2 = nt
    count += 1

#continue :

for i in range(5):
    if i == 3:
        continue
    print("hello",i)

#break :

for i in range(5):
    if i == 3:
        break
    print("hello",i)

#pass : use mostly in function and class

def fun():
    pass



