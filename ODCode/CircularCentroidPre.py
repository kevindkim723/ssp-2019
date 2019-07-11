import numpy as np
from astropy.io import fits
import math
im = fits.getdata('Aligned_reduced0000.fits')
image = np.array(im)

def centroidpre(x, y, r, m, bool):
    x = int(float(x))
    y = int(float(y))
    length = 2*r+1
    arrX = []
    arrY = []
    meanX = 0
    meanY = 0

    for row in range(length):
        ro = x-r+row
        for column in range(length):
            c = y-r+column
            if ((x-ro)**2 + (y-c)**2) > r**2:
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

#print(centroid(200,200,10,image))
