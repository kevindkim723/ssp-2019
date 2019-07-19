import numpy as np
from math import *
from BabyOD import *
from ephemeris import ephemeris2
from Gauss import *
T_DUE = 2458685.75

#i know it's terrible code but too late to fix xD
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
def correct(rvec, rvecdot, R, delta, t,ra,t0):
    rvecdot = list(rvecdot)
    
    print("RVEC: ", t)
    OE = babyOD2(rvec, rvecdot,t0)
    RAfit = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],t0,t[i],R)[1]
    
    print("FIT: ", RAfit)

    deltas = []
    parX = []
    parY = []
    parZ = []
    parXdot = []
    parYdot = []
    parZdot = []
    for i in range(len(t)):
        
        parX.extend(getdRAdX(rvec,rvecdot,R,delta,t[i],t0))
        parY.extend(getdRAdY(rvec,rvecdot,R,delta,t[i],t0))
        parZ.extend(getdRAdZ(rvec,rvecdot,R,delta,t[i],t0))
        parXdot.extend(getdRAdYdot(rvec,rvecdot,R,delta,t[i],t0))
        parYdot.extend(getdRAdYdot(rvec,rvecdot,R,delta,t[i],t0))
        parZdot.extend(getdRAdZdot(rvec,rvecdot,R,delta,t[i],t0))
        
        deltas.extend(abs(ra[i] - RAfit))
    

    masterArr = [[parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot],
                 [parX, parY,parZ, parXdot, parYdot,parZdot]]
    
    print("masterbate: ", masterArr)
    partialArr = [[parX],
                  [parY],
                  [parZ],
                  [parXdot],
                  [parYdot],
                  [parZdot]]
    for i in range(6):
        for j in range(6):
            masterArr[i][j] = np.dot(masterArr[i][j], partialArr[i])
        

    multArr = np.multiply(partialArr,deltaRA)
    finalArr = np.multiply(partialArr, masterArr)
    print("finallArR: ", finalArr)
    xyzArr = np.matmul(np.linalg.pinv(finalArr),multArr)
    return xyzArr
def diffcorrect(starterfile):
    r2, r2dot,t,R,ra,t0 = gauss2(starterfile)
    R = [[R[0]],
         [R[1]],
         [R[2]]]
    print(correct(r2,r2dot,R,10E-4,t, ra,t0))
    xyzArr = correct(r2,r2dot,R,10E-4,t, ra,t0)
    


diffcorrect("files/odstarter1.txt")
    
                 
