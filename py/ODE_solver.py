import numpy as np
from scipy.integrate import *

'''
Tank A
'''
TA0 = 90            # Temperature in tank A
VA0 = 5             # Volume at t = 0
PA = 0.7            # Base area

'''
Tank B
'''
TB0 = 10            # Temperature at t = 0
VB0 = 1             # Volume at t = 0
PB = 1.0            # Base area
DB = 0.00365665     # Drain gauge

'''
Water source
'''
FBin = 0.01         # Water flow velocity
TBin = 10           # Water temperature


'''
Physical constants
'''
a = 0.98            # Liquid viscosity
b = 0.63            # Liquid flux narrowing coefficient
g = 9.81            # Gravitational acceleration

t = np.linspace(0, 1000, 1000)
def ODEsystem(y, t, DA):
    if y[0] >= 0:
        FAout = - a * b * DA * np.sqrt(2 * g * y[0] / PA)
    else:
        FAout = 0
    dy2dt = - a * b * DB * np.sqrt(2 * g * y[1] / PB) + FBin - FAout
    dy3dt = (-FAout * (TA0 - y[2]) + FBin * (TBin - y[2])) / y[1]
    return [FAout, dy2dt, dy3dt]


def objective_function(DA):
    Vt = odeint(ODEsystem, [VA0, VB0, TB0], t, args=(DA,))
    TBmax = max(Vt[:, 2])
    return abs(TBmax - 50), Vt