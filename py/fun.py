import numpy

class funclass:

    def __init__(self):
        self.calls = 0

    def f1(self, x):
        self.calls +=1
        return -numpy.cos(0.1 * x) * numpy.exp(-((0.1 * x - 2 * numpy.pi) ** 2)) + 0.002 * (0.1 * x) ** 2



    def fcalls(self):
        return self.calls
    def zerocalls(self):
        self.calls = 0