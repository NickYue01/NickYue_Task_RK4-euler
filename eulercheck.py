# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:54:40 2022

@author: nicko
"""

# eulercheck.py
from odesolve import euler
# Defines the RHS of our ODE
def f (x , t ):
    return x
# Initial conditions
t0 = 1
x0 = 1
h = 0.5
t1 = t0 + h
x1 = euler ( f , x0 , t0 , h)
print ( ' Solving the ODE dx/dt = x ' )
print ( ' Initial condition x =' , x0 , 'when t =' , t0 )
print ( 'One step of the Euler method with a stepsize of h =' , h)
print ( ' Gives an estimate of x =' , x1 , 'when t =' , t1 )