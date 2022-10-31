from scipy.fft import fft, ifft 
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(x,(0,8),'constant',constant_values=(0))
N=14
n=np.arange(N)
un=(-1/2)**n
hn1=np.pad(un,(0,2),'constant',constant_values=(0))
hn2=np.pad(un,(2,0),'constant',constant_values=(0))
hn=hn1+hn2

X=fft(x)
H=fft(hn[:N])
Y=np.zeros(N)+1j*np.zeros(N)
for i in range(N):
    Y[i]=X[i]*H[i]
y=ifft(Y)

plt.stem(range(0,N),np.real(X))
plt.title("Using FFT")
plt.ylabel("$X(k)$")
plt.grid()
plt.show()

plt.stem(range(0,N),np.real(H))
plt.title("Using FFT")
plt.ylabel("$H(k)$")
plt.grid()
plt.show()

plt.stem(range(0,N),np.real(y))
plt.title("Using FFT and IFFT")
plt.ylabel("$y(n)$")
plt.grid()
plt.show()

