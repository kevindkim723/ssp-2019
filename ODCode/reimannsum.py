import math as m
def reimanncircle(x1,x2,r):
    step = .0001
    x = x1
    reimannsum = 0
    while (x < x2-step):
        reimannsum += (step * m.sqrt(r**2 - (x+step)**2))
        #print(r**2 - (x+step)**2)
        x+=step
    return reimannsum

print(reimanncircle(-2,2,2))
