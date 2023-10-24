from math import *

class funclass:

    def __init__(self):
        self.calls = 0

    def f1(self,x):
        return -cos(0.1 * x) * exp(-((0.1 * x - 2 * pi) ** 2)) + 0.002 * (0.1 * x) ** 2
        self.calls = self.calls + 1


    def fcalls(self):
        return self.calls
    def zerocalls(self):
        self.calls = 0
