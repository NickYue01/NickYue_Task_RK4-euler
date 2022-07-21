# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:12:46 2022

@author: nicko
"""
from odesolve import rk4
def f (x , t ):
    return x

t0 = 1
x0 = 1
h = 0.5
t1 = t0 + h
x1 = rk4 ( f , x0 , t0 , h)
print ( ' Solving the ODE dx/dt = x ' )
print ( ' Initial condition x =' , x0 , 'when t =' , t0 )
print ( 'One step of the Rk4 method with a stepsize of h =' , h)
print ( ' Gives an estimate of x =' , x1 , 'when t =' , t1 )