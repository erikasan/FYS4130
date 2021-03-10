import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize

alpha = 10
gamma = 10
V     = 1000
N     = 100000

def F(Nxy):
    Nx, Ny = Nxy
    res  = 0
    res += Nx*np.log(alpha*Nx/V)
    res += Ny*np.log(alpha*Ny/V)
    res += (N - Nx - Ny)*np.log(alpha*(N - Nx - Ny)/V)
    res += gamma/V*(Nx*Ny + (N - Nx - Ny)*(Nx + Ny))
    return res

def jac(Nxy):
    Nx, Ny = Nxy
    dFdNx = np.log(Nx/(N - Nx - Ny)) + gamma/V*(N - 2*Nx - Ny)
    dFdNy = np.log(Ny/(N - Nx - Ny)) + gamma/V*(N - Nx - 2*Ny)
    return dFdNx, dFdNy

x0 = np.array([10, 10])

res = scipy.optimize.minimize(fun=F, x0=x0, method='Nelder-Mead', jac=jac)
Nxy = res.x
