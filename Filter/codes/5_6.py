import numpy as np
import matplotlib.pyplot as plt
from sympy import N

n=np.arange(25)
un=(-1/2)**n

hn1=np.pad(un,(0,2),'constant',constant_values=(0))
hn2=np.pad(un,(2,0),'constant',constant_values=(0))

hn=hn1+hn2

nh=len(hn)
sum_hn=np.zeros(nh)
sum_hn[0]=hn[0]
for i in range(1,nh):
    sum_hn[i]=sum_hn[i-1]+hn[i]

plt.plot(range(len(hn)),sum_hn)
plt.ylabel("$\sum{h(n)}$")
plt.xlabel("$n$")
plt.grid()
plt.show()