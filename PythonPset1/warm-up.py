# Purpose of this code is to work with lists
# Exercise 0 (warm up)
# 6.21.2019
# Kevin Kim

def sumList(nums):
    sumnums = 0
    for n in nums:
        sumnums+=n
    return sumnums

print("testing sumList")
print(sumList([]))              # expected output: 0
print(sumList([3]))             # expected output: 3
print(sumList([1., 4.5, -3.2])) # expected output: 2.3

def estimatePi(n):
    counter = 0
    denom = 1
    pi = 0
    for a in range(n):
        if (counter%2 == 0):
            pi += 4/denom
        else:
            pi-= 4/denom
        denom+=2
        counter+=1
    return pi

print("testing estimatePi")
print(estimatePi(1))     # expected (approximate) output: 4.0
print(estimatePi(10))    # expected (approximate) output: 3.0418396189294032
print(estimatePi(100))   # expected (approximate) output: 3.1315929035585537
print(estimatePi(1000))  # expected (approximate) output: 3.140592653839794
print(estimatePi(10000)) # expected (approximate) output: 3.1414926535900345

def scaleVec(vec, scalar):
    vector = []
    for n in vec:
        vector.append(n * scalar)
    return vector

print("testing scaleVec")
vec = []
print(scaleVec(vec, 5)) # expected output: []
print(vec) # expected output: []
vec = [1]
print(scaleVec(vec, 5)) # expected output: [5]
print(vec) # expected output: [1]
vec = [-2, 1.5, 0.]
print(scaleVec(vec, 6)) # expected output: [-12., 9., 0.]
print(vec) # expected output: [-2, 1.5, 0.]
