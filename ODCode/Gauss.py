from math import *
import numpy as np


#helper method that converts equatorial vector into ecliptic vector
def ecliptic(x):
    EPSILON = rad(23.4358)
    transform = np.array([[1,0,0],
                          [0,m.cos(EPSILON), m.sin(EPSILON)],
                          [0,-m.sin(EPSILON), m.cos(EPSILON)]])
    return np.dot(transform, x)
#helper method to return magnitude of vector
def mag(x):
    return np.linalg.norm(x)

t1 = 2458292.73631
t2 = 2458309.74862
t3 = 2458317.726
ra1
ra2
ra3
dec1
dec2
dec3
rho1hat = ecliptic(np.array([cos(ra1) * cos(dec1), sin(ra1) * cos(dec1), sin(dec1)]))
rho2hat = ecliptic(np.array([cos(ra2) * cos(dec2), sin(ra2) * cos(dec2), sin(dec2)]))
rho3hat = ecliptic(np.array([cos(ra3) * cos(dec3), sin(ra3) * cos(dec3), sin(dec3)]))
R1 =
R2
R3
#defining d vectors from roh vectors
d0 = np.dot(rho1, np.cross(rho2hat, rho3))
d11 = np.dot(np.cross(R1, rho2hat), rho3)
d12 = np.dot(np.cross(R2, rho2hat), rho3)
d13 = np.dot(np.cross(R3, rho2hat), rho3)
d21 = np.dot(np.cross(rho1hat, R1), rho3)
d22 = np.dot(np.cross(rho1hat, R2), rho3)
d23 = np.dot(np.cross(rho1hat, R3), rho3)
d31 = np.dot(np.cross(rho2hat, R1), rho1)
d32 = np.dot(np.cross(rho2hat, R2), rho1)
d33 = np.dot(np.cross(rho2hat, R3), rho1)

k = 0.01720209895
nu  = k ** 2
tau1 = k * (t1 - t2)
tau3 = k * (t3 - t2)
tau = tau3 - tau1


#scalar equation of lagrange

A1 = tau3/tau
B1 = A1*(tau**2 - tau3**2)/6
A3 = -tau1/tau
B3 = A**3*(tau**2 - tau1**2)/6
A = (A1 * D21 - D22 + A3*D3)/-D0
B = (B1*D21 + B3 * D23)/-D0
E = -2*(np.dot(rho2hat, R2))
F = mag(R2) ** 2

a = -(A**2 + A*E + F)
b = -nu * (2*A*B + B * E)
c = -nu**2*B**2

polynomial = [1,0,a,0,0,b,0,0,c]
roots = np.roots(polynomial)

#removes all unreasonable roots 
for r2 in roots:
    rho2 = A + nu * B / r2 ** 3
    if abs(rho2) != rho2 or np.iscomplex(rho2)
        roots.remove(r2)
#finds proper r2 via taylor expansions of the f and g series
def iterate(r2, r2dot,nu,tau1, tau3):
    prevr2 = r2
    #if first pass (rdot is -1), solve second degree taylor series for f
    if (r2dot == -1):
        f1 = 1 - nu * tau1**2/(2*mag(r2)**3)
        f2 = 1 - nu * tau2**2/(2*mag(r2)**3)
        f3 = 1 - nu * tau3**2/(2*mag(r2)**3)
    #if subsequent pass, solve third degree taylor series for f
    else:
        f1 = 1 - nu * tau1**2/(2*mag(r2)**3) + tau1 * nu * np.dot(r2,r2dot)
        f2 = 1 - nu * tau2**2/(2*mag(r2)**3) + tau2 * nu * np.dot(r2,r2dot)
        f3 = 1 - nu * tau3**2/(2*mag(r2)**3) + tau3 * nu * np.dot(r2,r2dot)

    #g functions are taylor series to third degree
    g1 = tau1 - tau1 **3 nu/(6*r2**3)
    g2 = tau2 - tau2 **3 nu/(6*r2**3)
    g3 = tau3 - tau3 **3 nu/(6*r2**3)

    c1 = g3/(f1*g3 - g1 * f3)
    c3 = -g1/(f1*g3 - g1* f3)
    d1 = -f3/(f1*g3 - f3 * g1)
    d3 = f1/(f1*g3 - f3*g1)

    r1 = f1 * r2 + g1 * r2dot
    r3 = f3 * r2 + g3 * r2dot

    r2 = c1 * r1 + c2 * r3
    r2dot =

    
    














        
