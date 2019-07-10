import math as m
import numpy as np
from astropy.io import fits 
def skybackground(x, y, r1, r2, m): #pixel exclusive, calculates background of sky
    x = int(float(x))
    y = int(float(y))
    length = 2*r+1
    meanX = 0
    meanY = 0
    
    for row in range(length):
        ro = x-r+row
        for column in range(length):
            c = y-r+column
            if ((x-ro)**2 + (y-c)**2) > r**2 && ):
                m[c][ro] = 0
    for row in range(length):
        arrY.append(np.sum(m[row + y -r ,x-r:x+r+1]))
    for column in range(length):
        arrX.append(np.sum(m[y-r: y+r+1,column + x - r]))
    for v in range(len(arrX)):
        meanX += arrX[v] * (v + x-r)
    for v in range(len(arrY)):
        meanY += arrY[v] * (v + y-r)
    arrX = np.array(arrX)
    arrY = np.array(arrY)
    meanX = meanX / np.sum(arrX)
    meanY = meanY / np.sum(arrY)
    
         
    return meanX, meanY
