import numpy as np
import matplotlib.pyplot as plt

y=np.loadtxt('3_3_data_y.dat',dtype="double")
x=np.loadtxt('3_3_data_x.dat',dtype="double")

plt.subplot(2,1,1)
plt.stem(range(0,len(x)),x)
plt.title("Digital Filter Input-Output")
plt.ylabel("$x(n)$")
plt.grid()

plt.subplot(2,1,2)
plt.stem(range(0,len(y)),y)
plt.ylabel("$y(n)$")
plt.xlabel("$n$")
plt.grid()
plt.show()