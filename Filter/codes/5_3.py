import numpy as np
import matplotlib.pyplot as plt

n=np.arange(14)
un=(-1/2)**n

hn1=np.pad(un,(0,2),'constant',constant_values=(0))
hn2=np.pad(un,(2,0),'constant',constant_values=(0))

hn=hn1+hn2

plt.stem(range(0,len(hn)),hn)
plt.grid()
plt.ylabel("$h(n)$")
plt.xlabel("$n$")
plt.show()