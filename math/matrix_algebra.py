# Matrix Algebra

import numpy as np
from numpy import linalg as LA

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.matrix('6 2 -3 5')
v = np.matrix('3 5 -1 4')
w = np.matrix('1; 8; 0; 5')

#  Part 1
lst = [A, B, C, D, u, v, w]

for item in lst:
    print item.shape
    
# output: (2, 3)
# (2, 2)
# (3, 2)
# (2, 3)
# (1, 4)
# (1, 4)
# (4, 1) 

# Part 2
alpha = 6
lst = [u + v, u - v, alpha * u, u.dot(np.transpose(v)), LA.norm(u)]

for item in lst:
    print item
    
# output: [[ 9  7 -4  9]]
# [[ 3 -3 -2  1]]
# [[ 36  12 -18  30]]
# [[51]]
# 8.60232526704

# Part 3


try:
    print 'A + C = ', A + C
except:
    print 'A + C is not defined'
 # A + C =  A + C is not defined

try:
    print 'A - C^T = ', A - np.transpose(C)
except:
    print 'A - C^T is not defined'
 # A - C^T =  [[-4 -7 -3]
 #             [ 3  6  4]]

try:
    print 'C^T + 3 * D = ', np.transpose(C) + 3 * D
except:
    print 'C^T + 3D is not defined'
 # C^T + 3 * D =  [[14  3  3]
 #                 [ 2  7  9]]

try:
    print 'BA = ', B.dot(A)
except:
    print 'BA is not defined'
 # BA =  [[-1 -5 -1]
 #        [ 2  7  4]]

try:
    print 'BA^T = ', B.dot(np.transpose(A))
except:
    print 'BA^T is not defined'
 # BA^T =  BA^T is not defined
