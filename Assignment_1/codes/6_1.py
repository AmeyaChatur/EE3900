import numpy as np
import matplotlib.pyplot as plt

N=14
xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))
n=np.arange(N)

X=np.zeros(N) + 1j*np.zeros(N)
for k in range(N):
    for i in range(N):
        X[k]+=x[i]*np.exp(-1j*2*np.pi*k*i/N)
y=np.real(X)

un=(-1/2)**n
hn1=np.pad(un,(0,2),"constant",constant_values=(0))
hn2=np.pad(un,(2,0),"constant",constant_values=(0))
hn=hn1+hn2
H=np.zeros(N)+ 1j*np.zeros(N)
for k in range(N):
    for i in range(N):
        H[k]+=hn[i]*np.exp(-1j*2*np.pi*k*i/N)
h=np.real(H)

plt.subplot(2,1,1)
plt.stem(n,y)
# plt.title("FFT of $x(n)$")
# plt.xlabel("$k$")
plt.ylabel("$X(k)$")
plt.grid()

plt.subplot(2,1,2)
plt.stem(n,h)
# plt.title("FFT of $h(n)$")
plt.xlabel("$k$")
plt.ylabel("$H(k)$")
plt.grid()
plt.show()