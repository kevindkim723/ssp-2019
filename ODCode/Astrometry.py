import math as m
import numpy as np
from astropy.io import fits

#commented out code was code used testing code on Jaiden's values

from CircularCentroid import centroid
from CircularCentroidPre import centroidpre
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









#LSPR2(arrRA, arrDEC, arrX, arrY, 813.4701022025868, 449.373471013335)
def Astrometry(starterfile, imgfile, x,y, inclusive):
    #defining constants
    inclusive = inclusive == "True"
    radius1 = 10
    radius2 = 3
    astX = x
    astY = y
    arrRA = []
    arrDEC = []
    arrX = []
    arrY = []
    arrcentroidX = []
    arrcentroidY = []
    
    im = fits.getdata(imgfile)
    hdul = fits.open(imgfile)
    image = np.array(im)
    
    #parsing raw input into respective lists
    #assumes that each line in file is in format:
    #RA DEC X Y
    for line in open(starterfile,'r'):
        if ("#" in line):
            continue;
        line = line.strip("\n")
        arrline = line.split(" ")
        
        arrRA.append(float(arrline[0]))
        arrDEC.append(float(arrline[1]))
        arrX.append(arrline[2])
        arrY.append(arrline[3])
        
    #centroiding individual X and Y values from lists
    for i in range(len(arrX)):
        currx, curry = centroidpre(arrX[i],arrY[i],radius1, image,inclusive)
        arrcentroidX.append(currx)
        arrcentroidY.append(curry)
    #centroiding asteroid
    astX, astY = centroidpre(astX,astY, radius2,image,inclusive)
    #performing LSPR
    LSPR2(arrRA, arrDEC, arrcentroidX, arrcentroidY, astX, astY)
    print("DATE: ", hdul[0].header["DATE-OBS"].split("T")[0], "\nTIME: ",  hdul[0].header["DATE-OBS"].split("T")[1])
def main():
    starterfile = "files/"+ input("Enter name of starter file with .txt: ")
    imgfile = "files/" + input("Enter name of fits file with .fits: ")
    x = input("Xcoord of asteroid: ")
    y = input("Ycoord of asteroid: ")
    inclusive = input("Boolean of inclusivity: ")
    Astrometry(starterfile,imgfile,x,y,inclusive)

    
main()    
    
    

