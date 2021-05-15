# multi-dimensional array
'''
import numpy as np

a = np.array([
    [1, 23, 45, 8, 6, 3],
    [65, 96, 2, 6, 33, 99]
])

a2 = a.flatten()

a3 = a2.reshape(2, 2, 3)

print(a3)

# matrices


import numpy as np

aa = np.matrix('1 2 3 ; 4 5 6 ; 7 8 9')
ab = np.matrix('9 8 7 ; 6 5 4 ; 3 2 1')
m = ab * ab
print(aa, "\n", ab)
print(np.diagonal(m),"\n")
print(m)

'''
# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x3 matrix
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
# result is 3x4
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)