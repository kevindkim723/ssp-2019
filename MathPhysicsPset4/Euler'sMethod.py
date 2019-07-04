#Kevin Kim
#

import matplotlib.pyplot as plt
import numpy as np
def iterate(i,h):
    arrinit = np.array([[1],[0]])
    arrh = np.array([[1,h],[-h,1]])
    print(arrinit)
    for j in range(i):
        arrinit = np.matmul(arrh,arrinit)
        plt.plot(arrinit[0][0],arrinit[1][0], "ro")
    plt.show()


iterate(20,.5)
    



