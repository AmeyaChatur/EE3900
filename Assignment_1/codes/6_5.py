import numpy as np
import matplotlib.pyplot as plt


def convolutionToeplitz(x,h):
    mx=len(x)
    mh=len(h)
    Toeplitz=np.zeros((mx,mx+mh-1))
    for i in range(mx):
        htemp=np.pad(h,(i,mx-i-1),'constant',constant_values=(0))
        Toeplitz[i]=htemp
        # print(np.concatenate(Toeplitz,htemp,axis=0))
    # print(Toeplitz.T)
    y=np.matmul(Toeplitz.T,x)
    return y

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(x,(0,8),'constant',constant_values=(0))
N=14
n=np.arange(N)
un=(-1/2)**n
hn1=np.pad(un,(0,2),'constant',constant_values=(0))
hn2=np.pad(un,(2,0),'constant',constant_values=(0))
hn=hn1+hn2