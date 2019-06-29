# Trigonometry
# PROJECT
# Kevin Kim
# 6.27.2019
import math as m
# a function to determine the quadrant of an angle based on its sine and cosine (in radians)
# returns the angle in the correct quadrant (in radians)
def radian(c):
    return c*m.pi/180
def degree(x):
    return x*180/m.pi
def findQuadrant(sine, cosine):
    if cosine > 0 and sine > 0: #1
        return m.asin(sine)

    if cosine < 0 and sine > 0: #2
        return m.acos(cosine)

    if cosine < 0 and sine < 0: #3
        return pi - m.asin(sine)

    if cosine > 0 and sine < 0: #4
        return 2*pi + m.asin(sine)

# a function that given the values (in radians) of two sides and the included angle of a spheical triangle
# returns the values of the remaining side and two angles (in radians)
def SAS(a, B, c):
    print(a)
    a = radian(a)
    print(a)
    B = radian(B)
    c = radian(c)
    # YOUR CODE HERE (part a)
    b = m.acos(m.cos(a) * m.cos(c) + m.sin(a)*m.sin(a)*m.cos(B))
    C = m.asin(m.sin(c)*m.sin(B)/m.sin(b))
    A = m.asin(m.sin(a) * m.sin(B)/m.sin(b))
             
        
    return degree(b), degree(A), degree(C)

# YOUR CODE HERE (part b)

print(SAS(106,114,42))
