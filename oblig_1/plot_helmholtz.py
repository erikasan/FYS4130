import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

alpha = 10
gamma = 10
V     = 100
N     = 100000

def F(V, Nx, Ny, N):
    res  = 0
    res += Nx*np.log(alpha*Nx/V)
    res += Ny*np.log(alpha*Ny/V)
    res += (N - Nx - Ny)*np.log(alpha*(N - Nx - Ny)/V)
    res += gamma/V*(Nx*Ny + (N - Nx - Ny)*(Nx + Ny))
    return res

def r(phi):
    return -V/gamma*np.log(np.tan(phi))/(np.cos(phi) - np.sin(phi))

phi = np.linspace(0, np.pi/2, 10000)

Nx = r(phi)*np.cos(phi)
Ny = r(phi)*np.sin(phi)

sns.set()
plt.plot(phi, F(V, Nx, Ny, N))
plt.xlabel(r'$\varphi$ / Radians')
plt.ylabel(r'$F/T$')
plt.title(r'$\alpha=${} $\gamma=${} $V=${} $N=${}'.format(alpha, gamma, V, N))
plt.tight_layout()
plt.show()
