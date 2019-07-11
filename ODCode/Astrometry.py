import math as m
import numpy as np
from astropy.io import fits

#commented out code was code used testing code on Jaiden's values

from CircularCentroid import centroid
from LSPR import LSPR2
def RAtoDegree(sRA):
    sDeg = 0
    arr = sRA.split(":")
    for i in range(len(arr)):
        if i == 0:
            sDeg = sDeg + float(arr[i]) * 15
        else:
            sDeg = sDeg + 360 * float(arr[i])/(24 * 60 ** i)
    return sDeg
def DtoDegree(sD):
    sDeg = 0
    arr = sD.split(":")
    for i in range(len(arr)):
        if i == 0:
            sDeg = sDeg + float(arr[i]) 
        else:
            sDeg = sDeg + float(arr[i])/(60**i)
    return sDeg

#defining constants
radius1 = 10
radius2 = 3
astX = 622
astY = 403
arrRA = []
arrDEC = []
arrX = []
arrY = []
arrcentroidX = []
arrcentroidY = []


im = fits.getdata('june18.fits')
#im = fits.getdata('jaiden.fits')
image = np.array(im)

#parsing raw input into respective lists
for line in open('june18starter.txt','r'):
    line = line.strip("\n")
    arrline = line.split(" ")

    #print(arrline)
    arrRA.append(float(arrline[0]))
    arrDEC.append(float(arrline[1]))
    arrX.append(arrline[2])
    arrY.append(arrline[3])


##for line in open('row2.txt','r'):
##    arrline = line.split(" ")
##    arrX.append(arrline[0])
##    arrY.append(arrline[1])
##    arrRA.append(RAtoDegree(arrline[2]))
##    arrDEC.append(DtoDegree(arrline[3]))
    
    
#centroiding individual X and Y values from lists
for i in range(len(arrX)):
    currx, curry = centroid(arrX[i],arrY[i],radius1, image)
    arrcentroidX.append(currx)
    arrcentroidY.append(curry)
#centroiding asteroid
astX, astY = centroid(astX,astY, radius2,image)

#performing LSPR
print(LSPR2(arrRA, arrDEC, arrcentroidX, arrcentroidY, astX, astY))
#LSPR2(arrRA, arrDEC, arrX, arrY, 813.4701022025868, 449.373471013335)
def Astrometry(filename, 

    
    
    
    

