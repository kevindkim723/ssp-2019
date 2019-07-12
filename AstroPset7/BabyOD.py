import math as m
import numpy as np

def degree(x):
    x =  x * 180 / m.pi
    return x%360
def rad(x):
    return x * m.pi / 180
def mag(x):
    return np.linalg.norm(x)
def clamp(x):
    while (abs(x) != x):
        x=x+360
    return x
def ecliptic(x):
    EPSILON = rad(23.4358)
    transform = np.array([[1,0,0],
                          [0,m.cos(EPSILON), m.sin(EPSILON)],
                          [0,-m.sin(EPSILON), m.cos(EPSILON)]])
    return np.dot(transform, x)

def geta(rvec, rvecdot):
    return (2/mag(rvec) - np.dot(rvecdot, rvecdot))**-1

def gete(rvec, rvecdot,a):
    return m.sqrt(1- mag(np.cross(rvec, rvecdot))**2 / a)
#transform xyz equatorial vector into xyz ecliptic vector

def geti(hvec):
    return m.acos(hvec[2]/mag(hvec))
def getomega(hvec, i):
    hx = hvec[0]
    hy = hvec[1]
    magh = mag(hvec)
    sinomega = (hx/(magh * m.sin(i)))
    cosomega = (-hy/(magh * m.sin(i)))
    tanomega = sinomega/cosomega
    return m.atan2(sinomega, cosomega)

def getw(rvec,rvecdot,hvec, i, e, a,omega):
    rvec = ecliptic(rvec)
    rvecdot = ecliptic(rvecdot)
    rmag = mag(rvec)
    hmag = mag(hvec)
    sinu = rvec[2]/(rmag * m.sin(i))

    cosu = (rvec[0]*m.cos(omega) + rvec[1] * m.sin(omega))/rmag
    u = m.atan2(sinu, cosu)
    sinv = a*(1-e**2) * np.dot(rvec, rvecdot)/(rmag*hmag*e)
    cosv = (a*(1-e**2)/rmag -1 )/e
    v = m.atan2(sinv,cosv)
    
    return u-v, v
def getM(rvec, a, e,v):
    rvec = ecliptic(rvec)
    rmag = mag(rvec)
    E = degree(m.acos((1/e) * (1-rmag/a)))
    v = degree(v)
    if (0 <= v and v <= 180):
        if (E > 180):
            E = 360-E
    else:
        if (E < 180):
            E = 360 - E
    
    E = m.radians(E)
    return E - e*m.sin(E)
def getE(rvec, a, e, v):
    rvec = ecliptic(rvec)
    rmag = mag(rvec)
    E = degree(m.acos((1/e) * (1-rmag/a)))
    v = degree(v)
    if (0 <= v and v <= 180):
        if (E > 180):
            E = 360-E
    else:
        if (E < 180):
            E = 360 - E
    
    E = m.radians(E)
    return E
def getn(a):
    mu = (.01720209895)**2

    return m.sqrt(mu/a**3)
def getT(M,n,t):
    return t - M/n
def getP(n):
    return 2 * m.pi / (n * 365.25)
def babyOD(rvec, rvecdot, t):
    rvec = np.array(rvec)
    rvecdot = np.array(rvecdot)
    hvec = np.cross(ecliptic(rvec),ecliptic(rvecdot))
    a = geta(rvec,rvecdot)
    e = gete(rvec,rvecdot,a)
    i = geti(hvec)
    omega = getomega(hvec, i)
    w,v = getw(rvec,rvecdot, hvec, i,e,a, omega)
    M = getM(rvec,a,e,v)
    E = getE(rvec,a,e,v)
    n = getn(a)
    T = getT(M,n,t)
    P = getP(n)
    print("a = ", geta(rvec,rvecdot))
    print("e = ", gete(rvec, rvecdot,a ))
    print("i = ", degree(geti(hvec)))
    print("Ω = ", degree(omega))
    print("w = ", degree(w))
    print("M = ", degree(M))
    print("E = ", degree(E))
    print("n = ", n)
    print("T = ", T)
    print("P = ", P)

babyOD([0.26617801, -1.25968549, -0.38388658], [0.793688,0.18369241,0.38231058], 2458304.74796)
