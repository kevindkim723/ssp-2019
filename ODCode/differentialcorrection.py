import numpy as np
from math import *
from BabyOD import *
from ephemeris import *

T_DUE = 2458685.75

#i know it's terrible code but too late to fix xD
def getdRAdX(rvec, rvecdot, R, delta,t):
    rvec1 = rvec
    rvec2 = rvec
    rvec1[0] = rvec1[0] + delta
    rvec2[0] = rvec2[0] - delta
    OE = BabyOD2(rvec1, rvecdot,t)
    ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    OE = BabyOD2(rvec2, rvecdot,t)
    ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    return (ra1 - ra2)/(2*delta)
    
def getdRAdY(rvec, rvecdot, R, delta,t):
    rvec1 = rvec
    rvec2 = rvec
    rvec1[1] = rvec1[1] + delta
    rvec2[1] = rvec2[1] - delta
    OE = BabyOD2(rvec1, rvecdot,t)
    ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    OE = BabyOD2(rvec2, rvecdot,t)
    ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    return (ra1 - ra2)/(2*delta)
    
def getdRAdZ(rvec, rvecdot, R, delta,t):
    rvec1 = rvec
    rvec2 = rvec
    rvec1[2] = rvec1[2] + delta
    rvec2[2] = rvec2[2] - delta
    OE = BabyOD2(rvec1, rvecdot,t)
    ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    OE = BabyOD2(rvec2, rvecdot,t)
    ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    return (ra1 - ra2)/(2*delta)
    
def getdRAdXdot(rvec, rvecdot, R, delta,t):
    rvecdot1 = rvecdot
    rvecdot2 = rvecdot
    rvecdot1[0] = rvecdot1[0] + delta
    rvecdot2[0] = rvecdot2[0] - delta
    OE = BabyOD2(rvec, rvecdot1,t)
    ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    OE = BabyOD2(rvec2, rvecdot2,t)
    ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    return (ra1 - ra2)/(2*delta)
    
def getdRAdYdot(rvec, rvecdot, R, delta,t):
    rvecdot1 = rvecdot
    rvecdot2 = rvecdot
    rvecdot1[1] = rvecdot1[1] + delta
    rvecdot2[1] = rvecdot2[1] - delta
    OE = BabyOD2(rvec, rvecdot1,t)
    ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    OE = BabyOD2(rvec, rvecdot2,t)
    ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    return (ra1 - ra2)/(2*delta)
    
def getdRAdZdot(rvec, rvecdot, R, delta,t):
    rvecdot1 = rvecdot
    rvecdot2 = rvecdot
    rvecdot1[2] = rvecdot1[2] + delta
    rvecdot2[2] = rvecdot2[2] - delta
    OE = BabyOD2(rvec, rvecdot1,t)
    ra1 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    OE = BabyOD2(rvec2, rvecdot2,t)
    ra2 = ephemeris2(OE[0],OE[1],OE[2],OE[3],OE[4],OE[6],T_DUE,t,R)[1]
    return (ra1 - ra2)/(2*delta)
def correct(rvec, rvecdot, R, delta, t):
    dRAdX = getdRAdX(rvec,rveddot,R,delta,t)
    dRAdY
    dRAdZ
    dRAdYdot
    dRAdXdot
    dRAdZdot
