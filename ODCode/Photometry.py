import math as m
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

matrix = fits.getdata("aptest.FIT")
#returns -1 if not in aperture, 0 if border, 1 if inside pixel
def pixelType(x,y,r):
    counter = 0
    if (x**2 + y**2 > r**2):
        counter+=1
    if((x+1)**2 + y**2 > r**2):
        counter+=1
    if((x+1)**2 + (y+1)**2 > r**2):
        counter+=1
    if((x)**2 + (y+1)**2 > r**2):
        counter+=1

    if (counter == 4): #counter = 4 implies that all four corners of the pixel are not inside in the radius--> not a border nor inside pixel
        return -1
    if (counter == 0): # coutner = 0 implies that all four courners of the pixel are inside the radius--> must be inside pixel
        return 1
    return 0 # counter not equaling 4 or 0 means that it is a border pixel, as some corners are outside the radius and some corners are inside the radius.
    
def skybackground(x, y, r1, r2, m,inclusive): #pixel exclusive, calculates background of sky
    x = int(float(x))
    y = int(float(y))
    length = 2*r2+1
    arrSky = []
    m = m[y-r2:y+r2+1, x-r2:x+r2+1]
    print(len(m))
    for row in range(length):
        for column in range(length):
            if (((row-r2)**2 + (column-r2)**2) > (r1  ** 2) and (row-r2)**2 + (column-r2)**2 < r2**2):
                arrSky.append(m[row][column])
    #print(m)
   
    print("SKSKSKSK", np.mean(arrSky))
    plt.imshow(m)
    plt.show()
    return np.mean(arrSky)
    
def centroid(x,y,r,m,inclusive):
    length = 2 * r + 1
    m = m[y-r:y+r+1, x-r:x+r+1]
    for row in range(length):
        for column in range(length):
            if (pixelType(row-r, column-r,r) == 0):
                m[row][column] = 0
    plt.imshow(m)
    plt.show()
    print(m)
centroid(490,293, 12,matrix,True)

    

