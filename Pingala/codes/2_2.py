import numpy as np
import matplotlib.pyplot as plt

N=15
x=np.zeros(N)

x[0]=1
x[1]=1

for i in range(2,N):
    x[i]=x[i-1]+x[i-2]

plt.stem(range(N),x)
plt.ylabel("$x(n)$")
plt.grid()
plt.show()
