#Contains two ephemeris generators that both take in the orbital elements, time of observation, and the sun vector of observation to generate
#Right acension and declination for the observation in degrees
#ephemeris2() is the working version, not quite sure if I've fixed ephemeris() yet...
import math 
import numpy as np

#helper functions
def rad(x):
    x = float(x)
    return x * math.pi/180
def deg(x):
    x= float(x)
    x= math.degrees(x)
    return x%360

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

#constants
EPSILON = rad(23.4358)
mu = .01720209895

def solvekep(M,e):
    Eguess = M
    Eguess = Eguess - e*math.sin(Eguess)
    prevE = M
    while abs(Eguess - prevE) > 1e-4:
        prevE = Eguess
        Eguess = M + e*math.sin(Eguess)
    return Eguess

def ephemeris(a,e, I, h, w,m0, t0, t,R):
    print(m)
    E = solvekep(m)
    print(E)
    x = a*(math.cos(E) - e)
    y = a * (math.sqrt(1-e**2) * math.sin(E))
    print(y)
    z = 0
    vecxyz = np.mat([[x],[y],[z]])
    r1 = np.mat([[math.cos(w), -math.sin(w), 0],
                  [math.sin(w), math.cos(w), 0],
                  [0,0,1]])
    r2 = np.mat([[1,0,0],
                  [0,math.cos(I),-math.sin(I)],
                  [0,math.sin(I),math.cos(I)]])
    r3 = np.mat([[math.cos(h), -math.sin(h),0],
                   [math.sin(h), math.cos(h), 0],
                   [0,0,1]])
    vecXYZ = r3 * r2 * r1 * vecxyz
    print(vecXYZ)
    vecSun = R
    
    vecRho = (vecSun + vecXYZ)
    
    vecRhoHat = vecRho / np.linalg.norm(vecRho)
    
    rX = vecRhoHat[0][0]
    rY = vecRhoHat[1][0] * math.cos(EPSILON) - vecRhoHat[2][0] * math.sin(EPSILON)
    rZ = vecRhoHat[1][0] * math.sin(EPSILON) + vecRhoHat[2][0] * math.cos(EPSILON)
    



    dfinal = math.asin(rZ)
    afinal = math.atan2(rY,rX)
    
    return (dfinal), ((afinal))

def ephemeris2(a, e, I, h, w,m0, t0, t,R):
    n = mu / math.sqrt(a**3)

    I = rad(I)
    h = rad(h)
    
    w = rad(w)
    m0 = rad(m0)
    m = m0 + n*(t-t0)
    E = solvekep(m,e)
    x = a*(math.cos(E) - e)
    

    y = a * (math.sqrt(1-e**2) * math.sin(E))
    z = 0
    vecxyz = np.mat([[x],[y],[z]])

    r1 = np.mat([[math.cos(w), -math.sin(w), 0],
                  [math.sin(w), math.cos(w), 0],
                  [0,0,1]])
    r2 = np.mat([[1,0,0],
                  [0,math.cos(I),-math.sin(I)],
                  [0,math.sin(I),math.cos(I)]])
    r3 = np.mat([[math.cos(h), -math.sin(h),0],
                   [math.sin(h), math.cos(h), 0],
                   [0,0,1]])
    vecXYZ = r3 * r2 * r1 * vecxyz
    vecSun = R
    
    vecRho = (vecSun + vecXYZ)
    
    vecRhoHat = vecRho / np.linalg.norm(vecRho)
    
    rX = vecRhoHat[0][0]
    rY = vecRhoHat[1][0] * math.cos(EPSILON) - vecRhoHat[2][0] * math.sin(EPSILON)
    rZ = vecRhoHat[1][0] * math.sin(EPSILON) + vecRhoHat[2][0] * math.cos(EPSILON)
    

    dfinal = math.asin(rZ)
    afinal = math.atan2(rY,rX)
    return (deg(dfinal)), (deg(afinal%(math.pi * 2)))
