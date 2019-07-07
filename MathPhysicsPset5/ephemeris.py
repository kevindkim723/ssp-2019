import math 
import numpy as np

def rad(x):
    return x * math.pi/180
def deg(x):
    return x * 180 / math.pi
def degtohr(x):
    e1 = int(x/15)
    e2 = int((x/15 - int(x/15)) * 60)
    e3 = 60 * (((x/15 - int(x/15)) * 60) - int((x/15 - int(x/15)) * 60))
    return str(e1) + ":" + str(e2) + ":" + str(e3)
ee = rad(23.4358)
e = 0.6587595515873473
a = 3.092704185336301
I = rad(11.74759239647092)
h = rad(82.15763948051409)
w = rad(356.34109239)
m0 = 0.01246738682149958
t0 = 2458465.5
t = 2458668.5
mu = .01720209895
n = mu / math.sqrt(a**3)
m = m0 + n*(t - t0)

def solvekep(M):
    Eguess = M
    Mguess = Eguess - e* math.sin(Eguess)
    Mtrue = M
    while abs(Mguess - Mtrue) > 1e-004:
        Mguess = Eguess - e*math.sin(Eguess)
        Eguess = Eguess - (Mguess- Mtrue) / (1 - e*math.cos(Eguess))
    return Eguess
def ephemeris(e, a, I, h, w,m0, t0, t):
        
    E = solvekep(m)
    x = a*(math.cos(E) - e)
    y = a * (math.sqrt(1-e**2) * math.sin(E))
    z= 0
    vecxyz = np.mat([[x],[y],[z]])
    r1 = np.mat([[math.cos(w), -math.sin(w), 0],
                  [math.sin(w), math.cos(w), 0],
                  [0,0,1]])
    print(r1)
    r2 = np.mat([[1,0,0],
                  [0,math.cos(I),-math.sin(I)],
                  [0,math.sin(I),math.cos(I)]])
    print(r2)
    r3 = np.mat([[math.cos(h), -math.sin(h),0],
                   [math.sin(h), math.cos(h), 0],
                   [0,0,1]])
    vecXYZ = r3 * r2 * r1 * vecxyz
    print(vecXYZ)
    vecSun = np.mat([[-2.027522170125452e-01],
                     [9.963111621309770e-01],
                     [-6.498231666301151e-05]])
    vecRho = (vecSun + vecXYZ)
    vecRhoHat = vecRho / np.linalg.norm(vecRho)
    print(vecRhoHat)
    rX = vecRhoHat[0][0]
    rY = vecRhoHat[1][0] * math.cos(ee) - vecRhoHat[2][0] * math.sin(ee)
    rZ = vecRhoHat[1][0] * math.sin(ee) + vecRhoHat[2][0] * math.cos(ee)

    dfinal = math.asin(rZ)
    afinal = math.atan2(rY,rX)
    print(deg(dfinal))
    print(degtohr(deg(afinal)))
    return deg(dfinal), degtohr(deg(afinal))


