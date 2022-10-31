import numpy as np

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
x=[2,-1]
x=np.array(x)
h=[-1,2,1]
h=np.array(h)
print(convolutionToeplitz(x,h))