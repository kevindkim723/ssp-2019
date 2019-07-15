from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
from Photometry import photometry



def slopeError(arrX, regerror):
    arrX = np.array(arrX)
    arrX = arrX - np.mean(arrX)
    return regerror / sqrt(np.dot(arrX,arrX))

def interceptError(arrX, sloperror):
    arrX = np.array(arrX)
    n = len(arrX)
    sumXsq = np.dot(arrX,arrX)
    arrX = arrX - np.mean(arrX)
    return sloperror * sqrt(sumXsq/(n*np.dot(arrX,arrX)))
    

def PhotometricData(starterfile, imgfile):
    configureplot("m instrumental", "Vmag", "Vmag vs m instrumental")

    arrX = []
    arrY = []
    arrInstmag = []
    arrVmag = []
    for line in open(starterfile,'r'):
        if ("#" in line):
            line = line.strip("#")
            arrline = line.split(" ")
            x = (int(arrline[0]))
            y = (int(arrline[1]))
            aprad = int(arrline[2])
            anrad1 = int(arrline[3])
            anrad2 = int(arrline[4])
            Vmag = (float(arrline[5]))
            astinstmag = photometry(imgfile,x,y,aprad,anrad1,anrad2, True)[1]
            continue
        line = line.strip("\n")
        arrline = line.split(" ")
        x = (int(arrline[0]))
        y = (int(arrline[1]))
        aprad = int(arrline[2])
        anrad1 = int(arrline[3])
        anrad2 = int(arrline[4])
        Vmag = (float(arrline[5]))
        arrInstmag.append(photometry(imgfile,x,y,aprad,anrad1,anrad2, True)[1])
        arrVmag.append(Vmag)

    slope, yintercept,_,_ ,error = sp.linregress(arrInstmag, arrVmag)
    slopeerror = slopeError(arrInstmag, error)
    intercepterror = interceptError(arrInstmag, error)

    for i in range(len(arrInstmag)):
        plt.plot(arrInstmag[i], arrVmag[i], "ro")

    abline(slope, yintercept)
    print("Slope = ", slope)
    print("Y intercept =", yintercept)
    print("Slope Error = ", slopeerror)
    print("Intercept Error = ", intercepterror)
    print("Vmag Asteroid = ", astinstmag * slope + yintercept) 
    plt.show()



def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, 'b')
def configureplot(xlabel, ylabel, title):
    fig = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    fig.suptitle(title)

    


    
PhotometricData("files/june18pstarter.txt", "files/june18.fits")

    
    
