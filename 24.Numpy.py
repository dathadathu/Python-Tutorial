# numpy - numerical python
import numpy as np

# there are 6ways to create array

arr = np.array([1, 2, 3, 4, 5.0])

arr1 = np.linspace(1, 15, 16)  # 3 parts

arr2 = np.arange(1, 15, 3)  # step

arr3 = np.logspace(1, 40, 5)
print('%.2f' % arr3[4])

arr4 = np.zeros(5, int)
print(arr4)
arr5 = np.ones(6, float)
print(arr5)

# more on arrays

arr = np.array([1, 2, 3, 4, 5])
# adding 6 to all values in arrray
arr += 6

at = np.array([7, 8, 9, 10, 11])

# adding two arrays
print(arr + at)

# it is also known as vectorized operation

# perform mathematical operations

print(np.sort(arr))

# concatenate the arrays

print(np.concatenate([arr, at]))

# copying an array

a = arr
print(arr)
print(a)

aa = id(a)
ab = id(arr)

#this won't work address is point to same address

a = arr.view()
#shallow copy dynamically changes


#copy is a deep copy : it wont chnage the values


#Ex  : 1

import array as arr
b = arr.array('i',[1,2,3,4])
c = arr.array('i',[5,6,7,8])

for i in c:
    b.append(i)
    if len(c) == i:
        break

print(b)


#ex 2:
b = np.array([11,22,33,44])
max = np.array([0])

for k in range(0,len(b)):
    if (b[k] > max):
        max = b[k]

print(max)