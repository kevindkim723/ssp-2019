#Kevin Kim
#

import matplotlib.pyplot as plt
import numpy as np
def iterate(i,h):
    hvar = h**2/4
    arrinit = np.array([[1],[0]])
    arrh = np.array([[1-hvar,h],[-h,1-hvar]])
    print(arrinit)
    for j in range(i):
        
        arrinit = np.dot((1/(1+hvar)),np.matmul(arrh,arrinit))
        plt.plot(arrinit[0][0],arrinit[1][0], "ro")
    plt.show()


iterate(50,9)
    



