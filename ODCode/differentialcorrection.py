import numpy as np
from math import *
from BabyOD import *
from ephemeris import ephemeris2
from Gauss import *
T_DUE = 2458685.75

#i know it's terrible code but too late to fix xD

#returns partial of RA and DEC in respect to X
def getdRAdX(rvec, rvecdot, R, delta,t,t0):
    rvec = list(rvec)
    
    rvec1 = list.copy(rvec)
    rvec2 = list.copy(rvec)
    rvec1[0] = rvec1[0] + delta
    rvec2[0] = rvec2[0] - delta
    OE = babyOD2(rvec1, rvecdot,t)
    dec1, ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    OE = babyOD2(rvec2, rvecdot,t)
    dec2, ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    return (ra1 - ra2)/(2*delta), (dec1 - dec2)/(2*delta)

#returns partial of RA and DEC in respect to Y    
def getdRAdY(rvec, rvecdot, R, delta,t,t0):
    rvec = list(rvec)

    rvec1 = list.copy(rvec)
    rvec2 = list.copy(rvec)
    rvec1[1] = rvec1[1] + delta
    rvec2[1] = rvec2[1] - delta
    OE = babyOD2(rvec1, rvecdot,t)
    dec1, ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    OE = babyOD2(rvec2, rvecdot,t)
    dec2, ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    return (ra1 - ra2)/(2*delta), (dec1 - dec2)/(2*delta)

#returns partial of RA and DEC in respect to Z    
def getdRAdZ(rvec, rvecdot, R, delta,t,t0):
    rvec = list(rvec)
    rvec1 = list.copy(rvec)
    rvec2 = list.copy(rvec)
    rvec1[2] = rvec1[2] + delta
    rvec2[2] = rvec2[2] - delta
    OE = babyOD2(rvec1, rvecdot,t)
    dec1, ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    OE = babyOD2(rvec2, rvecdot,t)
    dec2, ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    return (ra1 - ra2)/(2*delta), (dec1 - dec2)/(2*delta)

#returns partial of RA and DEC in respect to X dot   
    
def getdRAdXdot(rvec, rvecdot, R, delta,t,t0):
    rvecdot = list(rvecdot)

    rvecdot1 = list.copy(rvecdot)
    rvecdot2 = list.copy(rvecdot)
    rvecdot1[0] = rvecdot1[0] + delta
    rvecdot2[0] = rvecdot2[0] - delta
    OE = babyOD2(rvec, rvecdot1,t)
    dec1, ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    OE = babyOD2(rvec, rvecdot2,t)
    dec2, ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    return (ra1 - ra2)/(2*delta), (dec1 - dec2)/(2*delta)
#returns partial of RA and DEC in respect to Y dot
    
def getdRAdYdot(rvec, rvecdot, R, delta,t,t0):
    rvecdot = list(rvecdot)
    rvecdot1 = list.copy(rvecdot)
    rvecdot2 = list.copy(rvecdot)
    rvecdot1[1] = rvecdot1[1] + delta
    rvecdot2[1] = rvecdot2[1] - delta
    OE = babyOD2(rvec, rvecdot1,t)
    dec1, ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
   
    OE = babyOD2(rvec, rvecdot2,t)
    dec2, ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    return (ra1 - ra2)/(2*delta), (dec1 - dec2)/(2*delta)

#returns partial of RA and DEC in respect to Z dot   
    
def getdRAdZdot(rvec, rvecdot, R, delta,t,t0):
    rvecdot1 = list.copy(rvecdot)
    rvecdot2 = list.copy(rvecdot)
    rvecdot1[2] = rvecdot1[2] + delta
    rvecdot2[2] = rvecdot2[2] - delta
    OE = babyOD2(rvec, [rvecdot[0], rvecdot[1] + delta, rvecdot[2]],t)
    dec1, ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    OE = babyOD2(rvec, rvecdot2,t)
    dec2, ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t,R)
    return (ra1 - ra2)/(2*delta), (dec1 - dec2)/(2*delta)

#RA should be in degrees
def correct(rvec, rvecdot, R, delta,ra,dec,t,t0):
    rvecdot = list(rvecdot)    
    deltas = []
    parX = []
    parY = []
    parZ = []
    parXdot = []
    parYdot = []
    parZdot = []
    for i in range(len(t)):
        OE = babyOD2(rvec, rvecdot,t0)

        DECfit,RAfit = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[5],t0,t[i],R)

        parX.extend(getdRAdX(rvec,rvecdot,R,delta,t[i],t0))
        parY.extend(getdRAdY(rvec,rvecdot,R,delta,t[i],t0))
        parZ.extend(getdRAdZ(rvec,rvecdot,R,delta,t[i],t0))
        parXdot.extend(getdRAdYdot(rvec,rvecdot,R,delta,t[i],t0))
        parYdot.extend(getdRAdYdot(rvec,rvecdot,R,delta,t[i],t0))
        parZdot.extend(getdRAdZdot(rvec,rvecdot,R,delta,t[i],t0))
        
        deltas.extend([abs(ra[i] - RAfit), abs(dec[i] - DECfit)])
    

    masterArr = [[parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot]]
    
    partialArr = [[parX],
                  [parY],
                  [parZ],
                  [parXdot],
                  [parYdot],
                  [parZdot]]
    for i in range(6):
        for j in range(6):
            masterArr[i][j] = np.dot(masterArr[i][j], partialArr[i][0])
        
    for i in range(6):
        partialArr[i][0] = np.dot(partialArr[i][0],deltas)
    
        
    finalArr = np.multiply(partialArr, masterArr)
    xyzArr = np.matmul(np.linalg.pinv(finalArr),partialArr)
    return xyzArr


def diffcorrect(starterfile):
    r2, r2dot,R,ra,dec,t,t0 = gauss2(starterfile)
    #parse sun vector into column vector
    R = [[R[0]],
         [R[1]],
         [R[2]]]
    print("******************************************** ", correct(r2,r2dot,R,10E-4,ra,dec,t,t0))
    #xyzArr = correct(r2,r2dot,R,10E-4,ra,dec,t,t0)
    


diffcorrect("files/odstarter1.txt")
    
                 
