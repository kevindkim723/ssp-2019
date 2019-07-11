import numpy as np
from astropy.io import fits
import math
import matplotlib.pyplot as plt
im = fits.getdata('Aligned_reduced0000.fits')
image = np.array(im)
def pixelType(x,y,r):
    counter = 0
    if (x**2 + y**2 < r**2):
        counter+=1
    if((x+1)**2 + y**2 < r**2):
        counter+=1
    if((x+1)**2 + (y-1)**2 < r**2):
        counter+=1
    if((x)**2 + (y-1)**2 < r**2):
        counter+=1

    if (counter == 4): #counter = 4 implies that all four corners of the pixel are inside in the radius--> must be completely inside pixel
        return -1
    if (counter == 0): # coutner = 0 implies that all four courners of the pixel are outside the radius--> must be outside aperture
        return 1
    return 0 # counter not equaling 4 or 0 means that it is a border pixel, as some corners are outside the radius and some corners are inside the radius.
def centroid(x, y, r, m):
    x = int(float(x))
    y = int(float(y))
    length = 2*r+1
    arrX = []
    arrY = []
    meanX = 0
    meanY = 0
    matrix = m[y-r:y+r+1, x-r:x+r+1]

    for row in range(length):
        for column in range(length):
            xcoord = column - r -.5
            ycoord = r + .5 - row
            if (pixelType(xcoord,ycoord,r)==1):
                matrix[row][column] = 0
 
    for row in range(length):
        arrY.append(np.sum(matrix[row ,0:length]))
    for column in range(length):
        arrX.append(np.sum(matrix[0: length, column]))
    for v in range(len(arrX)):
        meanX += arrX[v] * (v + x-r)
    for v in range(len(arrY)):
        meanY += arrY[v] * (v + y-r)
    arrX = np.array(arrX)
    arrY = np.array(arrY)
   
    meanX = meanX / len(arrX)
    meanY = meanY / len(arrY)
    
         
    return meanX, meanY
 
print(centroid(200,200,10,image))
