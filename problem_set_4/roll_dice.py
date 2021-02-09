import numpy as np
from dice import Dice

d6  = Dice(6)
d12 = Dice(12)

n = int(1e5)

dice6  = d6.roll(n)
dice12 = d12.roll(n)

mean6 = np.mean(dice6)
var6  = np.var(dice6)
std6  = np.std(dice6)

mean12 = np.mean(dice12)
var12  = np.var(dice12)
std12  = np.std(dice12)
