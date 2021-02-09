import numpy as np

class Dice:

    def __init__(self, S):
        self.S = S

    def mean(self):
        S = self.S
        return (S + 1)/2

    def var(self):
        S = self.S
        return (S + 1)*(S - 1)/12

    def std(self):
        var = self.var
        return np.sqrt(var())

    def roll(self, n):
        S = self.S
        return np.random.randint(1, S + 1, n)
