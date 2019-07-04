# Purpose of this code is to work with vector math in python
# Exercise 3 
# 6.21.2019
# Kevin Kim

def getMag(vec):
    mag = 0
    for n in vec:
        mag += n**2
    return mag**.5
def getDot(vecA, vecB):
    dot = 0
    n = 0
    for n in range(len(vecA)):
        dot += (vecA[n]*vecB[n])
    return dot
def getCross(vecA, vecB):
    vecC = [1,2,3]
    vecC[0] = vecA[1]*vecB[2] - vecB[1]*vecA[2]
    vecC[1] = vecA[2] * vecB[0] - vecB[2]*vecA[0]
    vecC[2] = vecA[0] * vecB[1] - vecB[0]*vecA[1]
    return vecC

print(getMag([]))
print(getMag([3]))
print(getMag([1,-1]))
print(getMag([1,1,1,1]))
print("**************")
print(getDot([],[]))
print(getDot([2,5,6],[3,7,8]))
print(getDot([1,-1,0],[-1,-1,5]))
print(getDot([1,0,1,0],[2,2,0,2]))
print("**************")
print(getCross([1,0,0],[0,1,0]))
print(getCross([1,0,0],[0,0,1]))
print(getCross([2,5,6],[3,7,8]))
