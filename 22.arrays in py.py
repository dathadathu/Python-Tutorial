# array :
import array as arr

vals = arr.array('u', ['b', 'j', 'i', 'o', 'p', 'u', 'm'])
print(sorted(vals))

# vals.reverse()

print(vals.buffer_info())

newArr = arr.array(vals.typecode, (a for a in vals))
for i in newArr:
    print(i)

print(newArr)

n = int(input('Number'))
F = 1
if n < 0:
    print('Not a Factorial Number')
elif n == 0:
    print('0 factorial is 1')
else:
    for i in range(1, n + 1):
        F = F * i
        print('The factorial of ', n, "is", F)