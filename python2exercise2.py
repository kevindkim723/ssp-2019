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


        
        

