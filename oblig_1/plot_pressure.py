import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

lb2gamma = 10
N = 20

def P(V):
    return 2/lb2gamma*(np.log(lb2gamma*N/V - 2) + lb2gamma/2*N/V + 1)

V = np.linspace(0.001, 2000, 100000)

sns.set()
plt.plot(V, P(V))
plt.show()
