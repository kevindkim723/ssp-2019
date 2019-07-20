import numpy as np
from math import *
from ephemeris import *
from BabyOD import *

arr = np.array([1,2,3])
arr = np.multiply(2,arr)
arr2 = np.array([5,6,7])
##print(arr-arr2)
##print(5E10)
##print(np.array([1,2,3]))
print(np.dot(arr,arr2))
print(float("+10"))
x = [1, 2,3, 4]
x[0] = x[0] + 5
print(x)
def fill(a):
    a[0] = a[0] +100000000

def two():
    return 1, 2
fill(x)
print("XX", x)
x[0] = x[0] + 1000
print(x)
print(np.dot(x,100))


arr1 = [[1],
        [2],
        [3]]
arr2 = [[5],
        [6],
        [7]]
print(np.multiply(500000000,arr2))
print(degrees(pi))

tent = []
tent.extend([10,10,101,1001010100,10])
print(tent)
print(np.multiply([[5,3],[5,1],[5,0]],[[3,2],[3,2],[3,2]]))
for x in range(5,8):
    print(x)
sunvec = [[-0.1567805100523754],
          [1.004571913998728],
          [-8.241513835712403e-05]]
r2 = [-0.04421857, -1.23734529,  0.15962511]
r2dot = [1.12155899, 0.09995605, 0.18390451]
t0 = 2458665.738722454

OE = babyOD2(r2, r2dot,t0)
        

DECfit,RAfit = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],40,t0,t0,sunvec)
print(DECfit)

