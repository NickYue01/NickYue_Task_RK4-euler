# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:11:59 2022

@author: nicko
"""


from odesolve import solveto, euler, rk4
#def f(x, t):
#    return x + t

def f(x, t):
    return x
 
x1 = -2
t1 = 1
t2 = 10
#hmax = 0.001
#x2 = solveto ( f, x1, t1, t2, hmax, method=euler)
#print(abs(x2 - (-11)) - 1e-10 / hmax**0.5)


#print ( ' Solving the ODE dx/dt = x ' )
#print ( ' Initial condition x =' , x1 , 'when t =' , t1 )
#print ( 'One step of the Rk4 method with a stepsize of h =' , hmax)
#print ( ' Gives an estimate of x =' , x2 , 'when t =' , t2 )

#solvero_euler
#xtrue = 2.71828182845905
#for h in [0.1, 0.01, 0.001, 0.003]:
    #xguess = solveto(f, 1, 0, 1, h)
    #print((xguess - xtrue) - 2*h)
    #print (abs(xguess - xtrue) < 2*h)


#solvero_euler
#xtrue = -11
#for h in [0.1, 0.01, 0.001, 0.003, 1e-5]:
#    xguess = solveto(f, -2, 1, 10, h)
#    print('LHS:', xguess+11)
#    print('RHS:', 1e-10 / h**0.5)
#    print('the difference:',abs(xguess - xtrue) - 1e-10 / h**0.5)
#    print( abs(xguess - xtrue) < 1e-10 / h**0.5)
    
#solveto_RK4
xtrue = 2.71828182845905
for h in [0.1, 0.01, 0.001, 0.003]:
    xguess = solveto(f, 1, 0, 1, h, rk4)
    print( abs(xguess - xtrue) < h**4)