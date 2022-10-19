import numpy as np
import matplotlib.pyplot as plt

N=14

x=[1,1]

for i in range(N):
    x.append(x[-1]+x[-2])

y=np.add(x[:N], x[2:])
plt.stem(range(N),y)
plt.grid()
plt.ylabel("$y(n)$")
plt.show()

