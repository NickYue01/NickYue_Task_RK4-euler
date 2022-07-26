# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:54:48 2022

@author: nicko
"""

import numpy as np
import matplotlib.pyplot as plt
from odesolve import odesolve
# Defines the RHS of our ODE
def f (X, t ):
    x,y = X
    dxdt = y
    dydt = -x
    
    return np.array([dxdt,dydt])
#Initial conditions
x0 = 1
y0 = 0
X0 = np.array([x0,y0])
h = 0.01 # max step size
t = np.linspace(0,10,100) # times to plot the solution
Xt = odesolve(f,X0,t,h)
#Use .T to transpose the array
plt.plot( t,Xt.T[0])
plt.plot(t,Xt.T[1])
plt.savefig('shm.pdf')
plt.show()
#print(t)