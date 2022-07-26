# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:38:31 2022

@author: nicko
"""

def euler(f, x, t, h):
    """Perform one step of the Euler method"""
    return x + (f (x , t ))*h
    pass


def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""
    k1 = f(x,t)
    k2 = f(x+k1*h*0.5, t+0.5*h)
    k3 = f(x+k2*h*0.5, t+0.5*h)
    k4 = f(x+k3*h, t+h)
    return x + ( k1 + 2*k2 + 2*k3 + k4 ) * h/6
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):         
    """Use many steps of method to get from x1,t1 to x2,t2"""
    
    the_loop = int((t2-t1)/hmax)
    reminder = t2 - t1 - the_loop*hmax
    
    x0 = x1
    t_middle = t1
    if the_loop == 0:
        x2 = x1
        
    for i in range (0,the_loop):                   
        if method == rk4:
            x2 = rk4 ( f , x0 , t_middle , hmax)
        else:
            x2 = euler ( f , x0 , t_middle , hmax)
        x0 = x2
        #print(t_middle)
        t_middle += hmax
        t_middle = round(t_middle,8)
    
    if reminder != 0:              
        if method == rk4:
            x2 = rk4 ( f , x0 , t2 , reminder)
        else:
            x2 = euler ( f , x0 , t2 , reminder)
     
    return x2
    pass

def f(x, t):
    return x + t

x1 = -2
t1 = 1
t2 = 10
hmax = 0.3
x2 = solveto ( f, x1, t1, t2, hmax, method=euler)
print(x2)
print(abs(x2 - (-11)) < 1e-10 / hmax**0.5)


#solvero_euler
#xtrue = -11
#for h in [0.1, 0.01, 0.001, 0.003, 1e-5]:
#    xguess = solveto(f, -2, 1, 10, h)
#    print('LHS:', xguess+11)
#    print('RHS:', 1e-10 / h**0.5)
#    print('the difference:',abs(xguess - xtrue) - 1e-10 / h**0.5)
#    print( abs(xguess - xtrue) < 1e-10 / h**0.5)
    