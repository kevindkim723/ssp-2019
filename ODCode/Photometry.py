#CODE ASSUMES CENTER OF CIRCULAR APERTURES IS IN THE CENTER OF A PIXEL
import math as math
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from CircularCentroid import centroid

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

def skybackground(x, y, r1, r2, matrix): #pixel inclusive, calculates background of sky
    x = int(float(x))
    y = int(float(y))
    length = 2*r2+1
    arrSky = []
    m = matrix[y-r2:y+r2+1, x-r2:x+r2+1]
    for row in range(length):
        for column in range(length):
            x = column - r2 -.5
            y = r2 + .5 - row
            if (pixelType(x,y,r1) == 1 and pixelType(x,y,r2) == -1):
                arrSky.append(m[row][column])

    return np.sum(arrSky)/len(arrSky) ,  len(arrSky)
 
 
def aperture(x,y,r,m,inclusive):
    matrix = m[y-r:y+r+1, x-r:x+r+1]
    length = 2*r+1
    sumVal = 0
    numPix = 0
    for row in range(length):
        for column in range(length):
            x = column - r -.5
            y = r + .5 - row
            if (inclusive):
                if (pixelType(x,y,r) == -1 or pixelType(x,y,r) == 0):

                    sumVal += matrix[row][column]
                    numPix += 1
            else:
                if (pixelType(x,y,r) == -1):
                    sumVal += matrix[row][column]
                    numPix += 1
            
    return sumVal, numPix
#centroid(489,292,10,matrix,True)

def photometry(filename, x,y,aprad,anrad1, anrad2, inclusive):
    GAIN = 0.8
    DARK = 10
    READ = 11

    
    m = fits.getdata(filename)    
    avgSky, nAN = skybackground(x,y,anrad1,anrad2,m)
    sumADU, nAP = aperture(x,y,aprad,m,inclusive)
    signal = (sumADU - nAP * avgSky)
    SNR = math.sqrt(signal* GAIN) / math.sqrt(1 + nAP*(1+nAP/nAN)*((avgSky * GAIN + DARK + READ ** 2 + GAIN**2/12)/(signal*GAIN)))
    instmag = -2.5* math.log10(signal)
    instuncertainty = 1.0857/SNR
    return signal, instmag, instuncertainty
    
    
    
    
def main():
    filename = input("Enter filename: ")
    x = input("x: ")
    y = input("y: ")
    aprad = input("aperture radius: ")
    anrad1 = input("annulus inner radius: ")
    anrad2 = input("annulus outer radius: ")
    print("Signal, instmag, instuncertainty: ", photometry("testfiles/aptest.FIT",92,284,3,5,10,True))
#main()

    

    
    

