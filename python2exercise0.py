# starter code for exercise 0 on programming homework 2

import numpy as np

fruits = np.array([["Apple","Banana","Blueberry","Cherry"],
["Coconut","Grapefruit","Kumquat","Mango"],
["Nectarine","Orange","Tangerine","Pomegranate"],
["Lemon","Raspberry","Strawberry","Tomato"]])

t1 = fruits[3][3] #a
print("a\n",t1)
t2 = fruits[1:3,1:3] #b
print("b\n",t2)
t3 = fruits[0::2]#c
print("c\n",t3)
t4 = fruits[1:3,1:3][::-1,::-1]
print("d\n", t4)
t5 = np.copy(fruits)
t5[:,0] = fruits[:,3]
t5[:,3] = fruits[:,0]
print("e\n",t5)
t6 = [["SLICED!" for a in fruits[:]] for x in fruits]
print("f\n",t6)

