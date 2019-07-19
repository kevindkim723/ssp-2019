import numpy as np
import math
#helper methods to help with number conversion
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
def degtohr(x):
    e1 = int(x/15)
    e2 = int((x/15 - int(x/15)) * 60)
    e3 = 60 * (((x/15 - int(x/15)) * 60) - int((x/15 - int(x/15)) * 60))
    return str(e1) + ":" + str(e2) + ":" + str(e3)
def dectodeg(x):
    e1 = int(x)
    e2 = int((x - int(x)) * 60)
    e3 = 60 * (((x - int(x)) * 60) - int((x - int(x)) * 60))
    return str(e1) + ":" + str(e2) + ":" + str(e3)

def LSPR(filename, x, y):
    #defining the arrays that will contain parsed values
    arrX = []
    arrY = []
    arrRA = []
    arrD = []
    #parsing text into arrays
    f = open(filename) #change this to filename later
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
        lineArr = line.split(" ")
        if(len(lineArr) > 1):
            arrX.append(lineArr[0])
            arrY.append(lineArr[1])
            arrRA.append(lineArr[2])
            arrD.append(lineArr[3])

    #converting RA and D to decimal values in degrees
    for i in range(len(arrRA)):
        arrRA[i] = RAtoDegree(arrRA[i])
    for i in range(len(arrD)):
        arrD[i] = DtoDegree(arrD[i])%360

    #converting to numpy
    arrX = np.array(arrX,dtype=float)
    arrY = np.array(arrY,dtype=float)
    arrRA = np.array(arrRA,dtype=float)
    arrD = np.array(arrD,dtype=float)

    #defining sums
    sum_x_times_y = np.dot(arrX, arrY)
    sum_x_squared = np.dot(arrX, arrX)
    sum_y_squared = np.dot(arrY, arrY)
    sum_x = np.sum(arrX)
    sum_y = np.sum(arrY)
    sum_RA = np.sum(arrRA)
    sum_RA_times_x = np.dot(arrRA, arrX)
    sum_RA_times_y = np.dot(arrRA, arrY)
    sum_D = np.sum(arrD)
    sum_D_times_x = np.dot(arrD, arrX)
    sum_D_times_y = np.dot(arrD, arrY)
    n = len(arrX)
    #defining the master arrays
    arrXYMaster = np.array([[n, sum_x, sum_y],[sum_x, sum_x_squared,sum_x_times_y],[sum_y, sum_x_times_y,sum_y_squared]])
    arrRAMaster = np.array([[sum_RA],[sum_RA_times_x],[sum_RA_times_y]])
    arrDMaster = np.array([[sum_D],[sum_D_times_x],[sum_D_times_y]])

    #performing LSPR to find plate constants
    arrOutput1 = np.array(np.matmul(np.linalg.inv(arrXYMaster), arrRAMaster))
    arrOutput2 = np.array(np.matmul(np.linalg.inv(arrXYMaster), arrDMaster))

    a11 = arrOutput1[1][0]
    a12 = arrOutput1[2][0]
    a21 = arrOutput2[1][0]
    a22 = arrOutput2[2][0]
    b1 = arrOutput1[0][0]
    b2 = arrOutput2[0][0]


    #matrix operations to find RA and D


    
   
    print(sum_x)
    print(sum_y)
    print(sum_RA)
    print(sum_D)

    RA = b1 + a11*x + a12 * y
    D = b2 + a21*x + a22*y

    print("RA: ", degtohr(RA))
    print("D: ", D)

    arrFitRA = np.array(np.dot(a11, arrX) + np.dot(a12,arrY)) + b1
    arrFitD = np.array(np.dot(a21, arrX) + np.dot(a22,arrY)) + b2

    uncertaintyRA = math.sqrt(1/(n-3) * np.linalg.norm(arrRA - arrFitRA)**2) * 3600
    uncertaintyD = math.sqrt(1/(n-3) * np.linalg.norm(arrD - arrFitD)**2) * 3600

    print(uncertaintyRA)
    print(uncertaintyD)
    return b1,b2,a11,a12,a21,a22,RA,D,uncertaintyRA,uncertaintyD

def LSPR2(arrRA, arrD, arrX, arrY,x,y):
    #converting to numpy
    arrX = np.array(arrX,dtype=float)
    arrY = np.array(arrY,dtype=float)
    arrRA = np.array(arrRA,dtype=float)
    arrD = np.array(arrD,dtype=float)

    #defining sums
    sum_x_times_y = np.dot(arrX, arrY)
    sum_x_squared = np.dot(arrX, arrX)
    sum_y_squared = np.dot(arrY, arrY)
    sum_x = np.sum(arrX)
    sum_y = np.sum(arrY)
    sum_RA = np.sum(arrRA)
    sum_RA_times_x = np.dot(arrRA, arrX)
    sum_RA_times_y = np.dot(arrRA, arrY)
    sum_D = np.sum(arrD)
    sum_D_times_x = np.dot(arrD, arrX)
    sum_D_times_y = np.dot(arrD, arrY)
    n = len(arrX)
    #defining the master arrays
    arrXYMaster = np.array([[n, sum_x, sum_y],[sum_x, sum_x_squared,sum_x_times_y],[sum_y, sum_x_times_y,sum_y_squared]])
    arrRAMaster = np.array([[sum_RA],[sum_RA_times_x],[sum_RA_times_y]])
    arrDMaster = np.array([[sum_D],[sum_D_times_x],[sum_D_times_y]])

    #performing LSPR to find plate constants
    arrOutput1 = np.array(np.matmul(np.linalg.inv(arrXYMaster), arrRAMaster))
    arrOutput2 = np.array(np.matmul(np.linalg.inv(arrXYMaster), arrDMaster))

    a11 = arrOutput1[1][0]
    a12 = arrOutput1[2][0]
    a21 = arrOutput2[1][0]
    a22 = arrOutput2[2][0]
    b1 = arrOutput1[0][0]
    b2 = arrOutput2[0][0]


    #matrix operations to find RA and D
   

   

    RA = b1 + a11*x + a12 * y
    D = b2 + a21*x + a22*y

    print("RA: ", degtohr(RA))
    print("D: ", dectodeg(D))

    arrFitRA = np.array(np.dot(a11, arrX) + np.dot(a12,arrY)) + b1
    arrFitD = np.array(np.dot(a21, arrX) + np.dot(a22,arrY)) + b2

    uncertaintyRA = math.sqrt(1/(n-3) * np.linalg.norm(arrRA - arrFitRA)**2) * 3600
    uncertaintyD = math.sqrt(1/(n-3) * np.linalg.norm(arrD - arrFitD)**2) * 3600

    print("uncertaintyRA:" , uncertaintyRA)
    print("uncertaintyD: " , uncertaintyD)
    return b1,b2,a11,a12,a21,a22,degtohr(RA),dectodeg(D),uncertaintyRA,uncertaintyD
