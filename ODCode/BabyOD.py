import math as m
import numpy as np

def degree(x):
    x =  x * 180 / m.pi
    return x%360
def rad(x):
    x= x * m.pi / 180
    return x % (2*m.pi)
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
    print("STEAKKKKKKKKKKKKKKKKKKKKKKKKK")
    return a, e, degree(i), degree(omega), degree(w),degree(M)

##babyOD([0.11507222713443244, -1.123393746613972, 0.09102871066613388]
##, [1.0419839550663161, 0.22149954021077756, -0.11425372540357415], 2458309.74862)



def geta2(rvec, rvecdot):
    return (2/mag(rvec) - np.dot(rvecdot, rvecdot))**-1

def gete2(rvec, rvecdot,a):
    return m.sqrt(1- mag(np.cross(rvec, rvecdot))**2 / a)
#transform xyz equatorial vector into xyz ecliptic vector

def geti2(hvec):
    return m.acos(hvec[2]/mag(hvec))
def getomega2(hvec, i):
    hx = hvec[0]
    hy = hvec[1]
    magh = mag(hvec)
    sinomega = (hx/(magh * m.sin(i)))
    cosomega = (-hy/(magh * m.sin(i)))
    tanomega = sinomega/cosomega
    return m.atan2(sinomega, cosomega)

def getw2(rvec,rvecdot,hvec, i, e, a,omega):
    rmag = mag(rvec)
    hmag = mag(hvec)
    sinu = rvec[2]/(rmag * m.sin(i))

    cosu = (rvec[0]*m.cos(omega) + rvec[1] * m.sin(omega))/rmag
    u = m.atan2(sinu, cosu)
    sinv = a*(1-e**2) * np.dot(rvec, rvecdot)/(rmag*hmag*e)
    cosv = (a*(1-e**2)/rmag -1 )/e
    v = m.atan2(sinv,cosv)
    
    return u-v, v
def getM2(rvec, a, e,v):
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
def getE2(rvec, a, e, v):
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
def getn2(a):
    mu = (.01720209895)**2

    return m.sqrt(mu/a**3)
def getT2(M,n,t):
    return t - M/n
def getP2(n):
    return 2 * m.pi / (n * 365.25)
def babyOD2(rvec, rvecdot, t):
    rvec = np.array(rvec)
    rvecdot = np.array(rvecdot)
    hvec = (np.cross((rvec),(rvecdot)))
    a = geta2(rvec,rvecdot)
    e = gete2(rvec,rvecdot,a)
    i = geti2(hvec)
    omega = getomega2(hvec, i)
    w,v = getw2(rvec,rvecdot, hvec, i,e,a, omega)
    M = getM2(rvec,a,e,v)
    E = getE2(rvec,a,e,v)
    n = getn2(a)
    T = getT2(M,n,t)
    P = getP2(n)
    precessedM = M + n*(2458685.75 - t)
    print("COFEONJADFOJDFASOJDFS: ", n*(2458685.75 - t))
    print("a = ", geta2(rvec,rvecdot))
    print("e = ", gete2(rvec, rvecdot,a ))
    print("i = ", degree(geti2(hvec)))
    print("Ω = ", degree(omega))
    print("w = ", degree(w))
    print("M = ", degree(M))
    print("E = ", degree(E))
    print("n = ", n)
    print("T = ", T)
    print("P = ", P)
    print("PrecessedM = ", degree(precessedM))
    return a, e, degree(i), degree(omega), degree(w),degree(M)

def main():
    babyOD2([.26617801, -1.25968549,-0.38388658], [.793688,0.18369241,.38231058], 2458304.74796)
    #babyOD([-0.52625769,  1.45365528, -0.12164782],[-0.68327862, -0.65363404,  0.15057236],2458665.833333)

#main()
