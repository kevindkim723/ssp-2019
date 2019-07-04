
##The overall goal of this exercise is to write a program that takes as input one of your
##asteroid images and returns the centroid of the asteroid.
##a. Write a program in python that finds the centroid of the data given in the above
##table. Check your result with what you obtained from your hand calculation.
##b. Now you will write a function to find the centroid of an object in an actual image. The
##function should take as parameters the filename of a FITS image, the x-coordinate of
##the asteroid, the y-coordinate of the asteroid, and a pixel radius to use in computer the
##centroid (four parameters in all). This function should:
##• Reads in the FITS image with the filename given
##• Performs a weighted average of the pixel coordinates centered on the given x-ycoordinates.
##These pixels should include the specified pixel as well as radius pixels
##in each direction. For example, a radius of 1 would result in a centroid of nine pixels
##centered on the x-y-coordinates.
##• Compute the uncertainty of the centroid in terms of the standard deviation of the
##mean in x and y
##• Return the x and y of the computed centroid and the x and y uncertainty (four
##values in all)
##You will use this function as part of your data reduction. It will be your primary way to
##determine the uncertainty in your centroids. For the provided sampleimage.fits, the
##asteroid 1951 Lick is about magnitude 17.5 and is located at 351,154. On this data, your
##function should values very close to these:
##Centroid: 350.9958 153.9956
##Uncertainty (std. dev. of the mean) in x,y: 0.005254018 0.005249733


import numpy as np
import math
from astropy.io import fits
im = fits.getdata('sampleimage.fits')
image = np.array(im)
c = [[0,33,21,33,8],
          [0,56,51,53,26],
          [23,120,149,73,18],
          [55,101,116,50,16],
          [11,78,26,2,10]]
matrix = np.array(c)
def getCentroid(m):
    arrX = []
    arrY =[]
    sumX = 0
    sumY = 0
    meanX = 0
    meanY = 0
    for row in range(len(m)):
        arrY.append(np.sum(m[row,:]))
    for column in range(len(m)):
        arrX.append(np.sum(m[:,column]))
    for v in range(len(arrX)):
        meanX += arrX[v] * v
    for v in range(len(arrY)):
        meanY += arrY[v] * v
    meanX = meanX / np.sum(arrX)
    meanY = meanY / np.sum(arrY)
    return meanX, meanY


def getCentroidFromFits(x, y, r, m):
    total = np.sum(m[x-r:x+r+1, y-r:y+r+1])
    length = 2*r+1
    arrX = []
    arrY =[]
    sumX = 0
    sumY = 0
    meanX = 0
    meanY = 0
    arrdevX = []
    arrdevY = []
    devX = 0
    devY= 0
    
    for row in range(length):
        arrY.append(np.sum(m[row+x-r,y-r:y+r+1]))
    for column in range(length):
        arrX.append(np.sum(m[x-r:x+r+1,column + y - r]))
    for v in range(len(arrX)):
        meanX += arrX[v] * (v + x-r)
    for v in range(len(arrY)):
        meanY += arrY[v] * (v + y-r)
        
    meanX = meanX / np.sum(arrX)
    meanY = meanY / np.sum(arrY)
    
    for v in range(len(arrX)):
        element = ((math.pow(meanX - (v + x - r) ,2) * arrX[v]))
        arrdevX.append(element)        
    for v in range(len(arrY)):
         element = ((math.pow(meanY - (v + y -r),2) * arrY[v]))
         arrdevY.append(element)
         
    devX = ((np.sum(arrdevX)/(total-1)) ** .5)/(math.sqrt(total))
    devY = (np.sum(arrdevY)/((total-1)*total)) ** .5
    
    return meanX, meanY, devX, devY

def getCentroidFromFits2(x,y,r,m):
    w,z = getCentroid(m[x-r:x+r+1, y-r:y+r+1])
    return w+x-r, z+y-r

print(getCentroidFromFits2(154,351,1,image),"Lol")
print(getCentroidFromFits(154,351,1,image))
print(getCentroidFromFits(2,2,2,matrix))


        
        

