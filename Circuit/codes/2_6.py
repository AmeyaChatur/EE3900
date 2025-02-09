import numpy as np
from matplotlib import pyplot as plt

def unitStep(t):
    if (t < 0): return 0
    elif (t == 0):return 0.5
    else: return 1

def v1(t):
    if (t >= 0): return 4/3*(1 - np.exp(-t*1.5e6))*unitStep(t)
    else: return 0

vc0 = np.vectorize(v1, otypes=['double'])
# print(vc0)
# vc1 = np.loadtxt('v1.txt')
t = np.linspace(0, 1e-5, 1000000)
plt.plot(t, vc0(t))
# plt.plot(vc1[:,0], vc1[:,1], '.')
plt.xlabel('t (s)')
plt.ylabel('$v_{C_0}(t)$ (V)')
plt.grid()
plt.legend(['Simulation', 'Analysis'])
plt.show()