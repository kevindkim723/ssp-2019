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
    arr = sD.split(": ")
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
print(RAtoDegree("14:36:38.97"))
#helper method to return magnitude of vector
def mag(x):
    return np.linalg.norm(x)







        
#time 1-3 of observation
t1 = 2458292.73631
t2 = 2458309.74862
t3 = 2458317.726
#right acension 1-3 of observation
ra1 = radians(RAtoDegree("14:36:38.97"))
ra2 = radians(RAtoDegree("14:50:17.94"))
ra3 = radians(RAtoDegree("15:03:24.30"))
dec1 = radians(11.343972)
dec2 = radians(4.748306)
dec3 = radians(0.493028)
#rho vectors
rho1 = []
rho2 = []
rho3 = []

#rho hat vectors in ecliptic 1 -3
rho1hat = ecliptic(np.array([cos(ra1) * cos(dec1), sin(ra1) * cos(dec1), sin(dec1)]))
rho2hat = ecliptic(np.array([cos(ra2) * cos(dec2), sin(ra2) * cos(dec2), sin(dec2)]))
rho3hat = ecliptic(np.array([cos(ra3) * cos(dec3), sin(ra3) * cos(dec3), sin(dec3)]))
#sun vectors R 1-3
R1 = np.array([-2.628087761997599E-02, 1.015991789539995E+00, -4.048203704214327E-05])
R2 = np.array([-3.091168712431013E-01, 9.685301616433887E-01, -4.256535119031212E-05])
R3 = np.array([-4.345237494735269E-01, 9.187388812811442E-01, -3.519915251166138E-05])
t =[]
ra = []
dec = []
R = []


def feed(starterfile):
     for line in open(starterfile,'r'):
        line = line.strip("\n")
        arrline = line.split(" ")
        time = arrline[3].split(":")
        t.append(convertJulian(arrline[0],arrline[1],arrline[2],time[0],time[1],time[2]))
        ra.append(radians(RAtoDegree(arrline[4])))
        dec.append(radians(DtoDegree(arrline[5])))
        R.append(np.array([float(arrline[6]),float(arrline[7]),float(arrline[8])]))
        
        


        
#r vectors
r1 = []
r2 = []
r3 = []
r1dot = []
r2dot = []
r3dot = []
#defining d vectors from roh vectors
D0 = np.dot(rho1hat, np.cross(rho2hat, rho3hat))
print("D0: ", D0)
print(R1)
print(rho2hat)

D11 = np.dot(np.cross(R1, rho2hat), rho3hat)
D12 = np.dot(np.cross(R2, rho2hat), rho3hat)
D13 = np.dot(np.cross(R3, rho2hat), rho3hat)
D21 = np.dot(np.cross(rho1hat, R1), rho3hat)
D22 = np.dot(np.cross(rho1hat, R2), rho3hat)
D23 = np.dot(np.cross(rho1hat, R3), rho3hat)
D31 = np.dot(np.cross(rho2hat, R1), rho1hat)
D32 = np.dot(np.cross(rho2hat, R2), rho1hat)
D33 = np.dot(np.cross(rho2hat, R3), rho1hat)

print("D11: ", D11)
k = 0.01720209895
nu  = k ** 2
tau1 = k * (t1 - t2)
tau3 = k * (t3 - t2)
tau = tau3 - tau1


#scalar equation of lagrange

A1 = tau3/tau
print("A1: ", A1)
B1 = A1*(tau**2 - tau3**2)/6
print("B1: ", B1)
A3 = -tau1/tau
B3 = A3*(tau**2 - tau1**2)/6
print("B3: ", B3)
A = (A1 * D21 - D22 + A3*D23)/-D0
B = (B1*D21 + B3 * D23)/-D0
E = -2*(np.dot(rho2hat, R2))
F = mag(R2) ** 2
print("B: ", B)

a = -(A**2 + A*E + F)
print("a: ", a)
b = -1 * (2*A*B + B * E)
print("b: ", b)
c = -1 * B**2

polynomial = [1,0,a,0,0,b,0,0,c]
roots = []

#removes all unreasonable roots 
for r2 in np.roots(polynomial):
    if abs(r2) == r2  and "0j" in str(r2):
        roots.append(r2)
print("SSS", roots)
def firstiterate(r2mag):
    r2mag = float(r2mag)
    global rho1,rho2,rho3

    tau1 = k * (t1 - t2)
    tau3 = k * (t3 - t2)
    #solve second degree taylor series for f
   
    f1 = 1 - tau1**2/(2 * r2mag**3)
    f3 = 1 - tau3**2/(2*r2mag**3)
    print("f1: ", f1)
    print("f3: ", f3)
    
    #g functions are taylor series to third degree
    g1 = tau1 - tau1 **3 /(6*r2mag**3)
    g3 = tau3 - tau3 **3 /(6*r2mag**3)
    print("g1: ", g1)
    print("g3: ", g3)


    #defining scalars c and d
    c1 = g3/(f1*g3 - g1 * f3)
    print("c1 first iteration: ", c1)
    c2 = -1
    c3 = -g1/(f1*g3 - g1* f3)
    print("c2 first iteration: ", c2)
    print("c3 first iteration: ", c3)

    d1 = -f3/(f1*g3 - f3 * g1)
    d3 = f1/(f1*g3 - f3*g1)
    print("D0 first iteration: ", D0)
    print("D11 first iteration: ", D11)
    print("D12 first iteration: ", D12)
    print("d1 first iteration: ", d1)
    print("d3 first iteration: ", d3)
    print("rhohat1: ", rho1hat)
    print("rhohat2: ", rho2hat)
    print("rhohat3: ", rho3hat)
    


    rho1mag = (c1 * D11 + c2 * D12 + c3*D13)/(c1 * D0)
    rho2mag = (c1 * D21 + c2*D22 + c3 * D23)/(c2*D0)
    rho3mag = (c1 * D31 + c2*D32 + c3*D33)/(c3*D0)
   
    rho1 = np.multiply(rho1mag,rho1hat)
    rho2 = np.multiply(rho2mag,rho2hat)
    rho3 = np.multiply(rho3mag,rho3hat)

    #calculating r1,r2,r3 from the fundamental triangle using sun vector and rho vectors
    r1 = rho1 - R1
    r2 = rho2 - R2
    r3 = rho3 - R3
    r2dot = np.multiply(r1,d1) + np.multiply(d3,r3)

    
    print("r2 1st iteratoin: ", r2)
    print("r2dotmag 1st iteration: ", r2dot)
    
    return r2,r2dot

#finds proper r2 via taylor expansions of the f and g series
def iterate(r2,r2dot):
    global rho1,rho2,rho3
    t1mod = t1 - mag(rho1)/C
    t2mod = t2 - mag(rho2)/C
    t3mod = t3 - mag(rho3)/C
    print("r2: ",r2)
    
    tau1 = k * ( t1mod - t2mod)
    print("tau1: ", tau1)
    tau3 = k * (t3mod - t2mod)
    print("tau3: ", tau3)

    magprevr2 = mag(r2)
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
    print("f1: ", f1)
    print("f3: " , f3)
    print("g1: ", g1)
    print("g3: ", g3)
    #defining scalars c and d
    c1 = g3/(f1*g3 - g1*f3)
    c2 = -1
    c3 = -g1/(f1*g3 - g1*f3)
    
    d1 = -f3/(f1*g3 - f3 * g1)
    d3 = f1/(f1*g3 - f3*g1)
    print("D0 other iteration: ", D0)
    print("D11 other iteration: ", D11)
    print("D12 other iteration: ", D12)
    print("D13 other iteration: ", D13)
    print("D22 other iteration: ", D22)
    print("d3 other iteration: ", d3)
    print("c2 other iteration: ", c2)
    print("c3 other iteration: ", c3)
    print("d1 other iteration: ", d1)
    print("d3 other iteration: ", d3)
    print("c2 other iteration: ", c2)
    rho1mag = (c1 * D11 + c2*D12 + c3*D13)/(c1 * D0)
    rho2mag = (c1 * D21 + c2*D22 + c3 * D23)/(c2*D0)
    rho3mag = (c1 * D31 + c2*D32 + c3*D33)/(c3*D0)
    print("rho1mag other iteration: ", rho1mag)
    rho1 = np.multiply(rho1mag,rho1hat)
    print("rho1 other iteration: ", rho1)

    rho2 = np.multiply(rho2mag,rho2hat)
    rho3 = np.multiply(rho3mag,rho3hat)

    #calculating r1,r2,r3 from the fundamental triangle using sun vector and rho vectors
    r1 = rho1 - R1
    r2 = rho2 - R2
    r3 = rho3 - R3
    r2dot = np.multiply(r1,d1) + np.multiply(d3,r3)
    
    if (abs(mag(r2) - magprevr2) < 10E-5):
        return r2,r2dot
    return iterate(r2, r2dot)

rvec, rdotvec = firstiterate(roots[0])
print("magrev: ", mag(rvec))
print("magrdotvec: ", mag(rdotvec))
finalr, finalr2 = iterate(rvec,rdotvec)
print(mag(finalr))
print("final r list: ", finalr.tolist())
print("Final r2dot: " ,finalr2.tolist())
babyOD2(finalr.tolist(), finalr2.tolist(), t2)


        
