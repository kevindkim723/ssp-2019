#CODE ASSUMES CENTER OF CIRCULAR APERTURES IS IN THE CENTER OF A PIXEL
import math as m
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

matrix = fits.getdata("aptest.FIT")
#helper method to print matrix in easy to see format
def pltprint(m):
    plt.imshow(m)
    plt.show()

#returns -1 if in aperture, 0 if border, 1 if not in aperture
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


def skybackground(x, y, r1, r2, m,inclusive): #pixel exclusive, calculates background of sky
    x = int(float(x))
    y = int(float(y))
    length = 2*r2+1
    arrSky = []
    m = m[y-r2:y+r2+1, x-r2:x+r2+1]
    print(len(m))
    for row in range(length):
        for column in range(length):
            x = column - r2 -.5
            y = r2 + .5 - row
            if (pixelType(x,y,r1) == 1 and pixelType(x,y,r2) == -1):
                arrSky.append(m[row][column])
                m[row][column] = 10000
    #print(m)
    print(len(arrSky))
    pltprint(m)
    #print("mean: ", np.mean(arrSky))
 
    
def centroid(x,y,r,m,inclusive):
    length = 2*r+1
    m = m[y-r:y+r+1, x-r:x+r+1]
    print(len(m))
    for row in range(length):
        for column in range(length):
            x = column - r -.5
            y = r + .5 - row
            if (pixelType(x,y,r) == 0):
                m[row][column] = 0
    pltprint(m)
#centroid(489,292,10,matrix,True)

skybackground(490,293,8,13,matrix,True)
    

