import numpy as np
import matplotlib.pyplot as plt
from sympy import N

n=np.arange(14)
un=(-1/2)**n

hn1=np.pad(un,(0,2),'constant',constant_values=(0))
hn2=np.pad(un,(2,0),'constant',constant_values=(0))

hn=hn1+hn2

nh=len(hn)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)

y=np.zeros(nx+nh-1)
for k in range(nx+nh-1):
    for n in range(nh):
        if 0<=k-n<nx:
            y[k]+=x[k-n]*hn[n]

plt.stem(range(0,nx+nh-1),y)
plt.ylabel("$y(n)$")
plt.xlabel("$n$")
plt.grid()
plt.show()