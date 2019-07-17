from math import *
import numpy as np
from BabyOD import *

EPSILON = radians(23.4358)
C = 173.145
#converts into julian date
def convertJulian(year, month, date, hour, minute, second):
    year = float(year)
    month = float(month)
    date = float(date)
    hour = float(hour)
    minute = float(minute)
    second = float(second)
    J = 367 * year -int(7*(year + int((month+9)/12))/4) + int(275*month/9) + date + 1721013.5
    time = hour + minute/60 + second/3600
    return J + time/24

#helper method that converts equatorial vector into ecliptic vector
def ecliptic(x):
    x = np.array(x)
    transform = np.array([[1,0,0],
                          [0,cos(EPSILON), sin(EPSILON)],
                          [0,-sin(EPSILON), cos(EPSILON)]])
    return np.dot(transform, x)
#helper method to convert right acension into decimal degree
def RAtoDegree(sRA):
    sDeg = 0
    isnegative = False
    arr = sRA.split(":")
    if ("-" in sRA):
        isnegative = True
    for i in range(len(arr)):
        if i == 0:
            sDeg = sDeg + float(arr[i]) * 15
        else:
            if (isnegative):
                sDeg = sDeg - 360 * float(arr[i])/(24 * 60 ** i)
            else:
                sDeg = sDeg + 360 * float(arr[i])/(24 * 60 ** i)
    return sDeg
#helper method to convert sexagesimal to decimal degree
def DtoDegree(sD):
    sDeg = 0
    arr = sD.split(":")
    isnegative = False
    if ("-" in sD):
        isnegative = True
    for i in range(len(arr)):
        if i == 0:
            
            sDeg = sDeg + float(arr[i]) 
        else:
            if (isnegative):
                sDeg = sDeg - float(arr[i])/(60**i)

            else:
                sDeg = sDeg + float(arr[i])/(60**i)
    return sDeg

#helper method to return magnitude of vector
def mag(x):
    return np.linalg.norm(x)




rho1hat = []
rho2hat = []
rho3hat = []
#rho vectors
rho1 = []
rho2 = []
rho3 = []
t =[]
ra = []
dec = []
R = []
k = 0.01720209895
D0 = 0
D11 = 0
D12 = 0
D13 = 0
D21 = 0
D22 = 0
D23 = 0
D31 = 0
D32 = 0
D33 = 0


def feed(starterfile):
    global rho1hat,rho2hat,rho3hat
    for line in open(starterfile,'r'):
        line = line.strip("\n")
        arrline = line.split(" ")
        time = arrline[3].split(":")
        t.append(convertJulian(arrline[0],arrline[1],arrline[2],time[0],time[1],time[2]))
        ra.append(radians(RAtoDegree(arrline[4])))
        dec.append(radians(DtoDegree(arrline[5])))
        R.append(np.array([float(arrline[6]),float(arrline[7]),float(arrline[8])]))
    #rho hat vectors in ecliptic 1 -3
    rho1hat = ecliptic(np.array([cos(ra[0]) * cos(dec[0]), sin(ra[0]) * cos(dec[0]), sin(dec[0])]))
    rho2hat = ecliptic(np.array([cos(ra[1]) * cos(dec[1]), sin(ra[1]) * cos(dec[1]), sin(dec[1])]))
    rho3hat = ecliptic(np.array([cos(ra[2]) * cos(dec[2]), sin(ra[2]) * cos(dec[2]), sin(dec[2])]))
        
        

def findroots(starterfile):
    global D0,D11,D12,D13,D21,D22,D23,D31,D32,D33
    feed(starterfile)
    dec[0] = radians(11.343972)
    dec[1] = radians(4.748306)
    dec[2] = radians(0.493028)
   


    dec1 = radians(11.343972)
    dec2 = radians(4.748306)
    dec3 = radians(0.493028)

   
    #defining d vectors from roh vectors
    D0 = np.dot(rho1hat, np.cross(rho2hat, rho3hat))

    D11 = np.dot(np.cross(R[0], rho2hat), rho3hat)
    D12 = np.dot(np.cross(R[1], rho2hat), rho3hat)
    D13 = np.dot(np.cross(R[2], rho2hat), rho3hat)
    D21 = np.dot(np.cross(rho1hat, R[0]), rho3hat)
    D22 = np.dot(np.cross(rho1hat, R[1]), rho3hat)
    D23 = np.dot(np.cross(rho1hat, R[2]), rho3hat)
    D31 = np.dot(np.cross(rho2hat, R[0]), rho1hat)
    D32 = np.dot(np.cross(rho2hat, R[1]), rho1hat)
    D33 = np.dot(np.cross(rho2hat, R[2]), rho1hat)

    nu  = k ** 2
    tau1 = k * (t[0] - t[1])
    tau3 = k * (t[2] - t[1])
    tau = tau3 - tau1


    #scalar equation of lagrange
    A1 = tau3/tau
    B1 = A1*(tau**2 - tau3**2)/6
    A3 = -tau1/tau
    B3 = A3*(tau**2 - tau1**2)/6
    A = (A1 * D21 - D22 + A3*D23)/-D0
    B = (B1*D21 + B3 * D23)/-D0
    E = -2*(np.dot(rho2hat, R[1]))
    F = mag(R[1]) ** 2

    a = -(A**2 + A*E + F)
    b = -1 * (2*A*B + B * E)
    c = -1 * B**2

    polynomial = [1,0,a,0,0,b,0,0,c]
    roots = []

    #removes all unreasonable roots 
    for r2 in np.roots(polynomial):
        if abs(r2) == r2  and "0j" in str(r2):
            roots.append(r2)
    return roots
def firstiterate(r2mag):
    r2mag = float(r2mag)
    global rho1,rho2,rho3

    tau1 = k * (t[0] - t[1])
    tau3 = k * (t[2] - t[1])

    #solve second degree taylor series for f
    f1 = 1 - tau1**2/(2 * r2mag**3)
    f3 = 1 - tau3**2/(2*r2mag**3)
    
    
    #g functions are taylor series to third degree
    g1 = tau1 - tau1 **3 /(6*r2mag**3)
    g3 = tau3 - tau3 **3 /(6*r2mag**3)
   

    #defining scalars c and d
    c1 = g3/(f1*g3 - g1 * f3)
    c2 = -1
    c3 = -g1/(f1*g3 - g1* f3)

    d1 = -f3/(f1*g3 - f3 * g1)
    d3 = f1/(f1*g3 - f3*g1)
 
    rho1mag = (c1 * D11 + c2 * D12 + c3*D13)/(c1 * D0)
    rho2mag = (c1 * D21 + c2*D22 + c3 * D23)/(c2*D0)
    rho3mag = (c1 * D31 + c2*D32 + c3*D33)/(c3*D0)
   
    rho1 = np.multiply(rho1mag,rho1hat)
    rho2 = np.multiply(rho2mag,rho2hat)
    rho3 = np.multiply(rho3mag,rho3hat)

    #calculating r1,r2,r3 from the fundamental triangle using sun vector and rho vectors
    r1 = rho1 - R[0]
    r2 = rho2 - R[1]
    r3 = rho3 - R[2]
    
    r2dot = np.multiply(r1,d1) + np.multiply(d3,r3)
    return r2,r2dot

#finds proper r2 via taylor expansions of the f and g series
def iterate(r2,r2dot, bound):
    global rho1,rho2,rho3
    
    magprevr2 = mag(r2)

    t1mod = t[0] - mag(rho1)/C
    t2mod = t[1] - mag(rho2)/C
    t3mod = t[2] - mag(rho3)/C
    
    tau1 = k * ( t1mod - t2mod)
    tau3 = k * (t3mod - t2mod)

    #constants for taylor polynomials
    u =  1 / mag(r2)**3
    z = np.dot(r2,r2dot)/mag(r2)**2
    q = np.dot(r2dot,r2dot)/(mag(r2)**2) - u

    #f functions are taylor series to the fourth degree
    f1 = 1 - u * tau1**2 /2 + (u*z * tau1**3)/2 + (3*u*q - 15*u*z**2+u**2) * (tau1**4)/24
    f3 = 1 - u * tau3**2 /2 + (u*z * tau3**3)/2 + (3*u*q - 15*u*z**2+u**2) * (tau3**4)/24

    #g functions are taylor series to fourth degree
    g1 = tau1 - (u*tau1**3)/6 + (u*z * tau1**4)/4
    g3 = tau3 - (u*tau3**3)/6 + (u*z * tau3**4)/4
    
    #defining scalars c and d
    c1 = g3/(f1*g3 - g1*f3)
    c2 = -1
    c3 = -g1/(f1*g3 - g1*f3)
    
    d1 = -f3/(f1*g3 - f3 * g1)
    d3 = f1/(f1*g3 - f3*g1)
   
    rho1mag = (c1 * D11 + c2*D12 + c3*D13)/(c1 * D0)
    rho2mag = (c1 * D21 + c2*D22 + c3 * D23)/(c2*D0)
    rho3mag = (c1 * D31 + c2*D32 + c3*D33)/(c3*D0)
   
    rho1 = np.multiply(rho1mag,rho1hat)
    rho2 = np.multiply(rho2mag,rho2hat)
    rho3 = np.multiply(rho3mag,rho3hat)

    #calculating r1,r2,r3 from the fundamental triangle using sun vector and rho vectors
    r1 = rho1 - R[0]
    r2 = rho2 - R[1]
    r3 = rho3 - R[2]
    
    r2dot = np.multiply(r1,d1) + np.multiply(d3,r3)
    if (abs(mag(r2) - magprevr2)) < (bound):
        return r2,r2dot
    return iterate(r2, r2dot,bound)
def main():
    
    roots = findroots("files/odstarter1.txt")
    index = input("which root (1,2,3) ")
    rvec, rdotvec = firstiterate(roots[0])
    bound = -1 * int(input("to what bound? 10E-: "))
    bound = 10**(bound)
    finalr, finalr2 = iterate(rvec,rdotvec,bound)
    babyOD2(finalr.tolist(), finalr2.tolist(), t2)

main()
