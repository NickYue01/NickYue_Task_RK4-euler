# odesolve.py
#
# Author: <Ziqi Yue>
# Date:   <20220721>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

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
    
    the_loop = int(round((t2-t1)/hmax))
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


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    t0 = t[0]
    tmax = t[-1]
    xt =[]
    #used for when the array only contains one element, the program will report: can't multiply sequence by non-int of type 'float'.
    #use my_try to choose the array which only contains one element. my_try will not use again in the further program.
    try:
        my_try = X0[1]      
    except:
        X0 = X0[0]
    for i in t:
        my_x = solveto(f,X0,t0,i,hmax,method)
        xt.append(my_x)
    xt = np.array(xt)

  
    return xt
    pass

import numpy as np
import matplotlib.pyplot as plt
#Defines the RHS of our ODE
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

def f(x, t):
        return x
x0 = [1]
tvals = np.linspace(0, 1, 5)
expected_euler = np.array([[1. , 1.28386503, 1.64830942, 2.11620682, 2.71692393]])
expected_rk4   = np.array([[1. , 1.28402542, 1.64872127, 2.11700002, 2.71828183]])
guess_euler = odesolve(f, x0, tvals, 0.001, euler)
guess_rk4   = odesolve(f, x0, tvals, 0.001, rk4)
#print(np.allclose(expected_euler, guess_euler))
print(np.allclose(expected_rk4, guess_rk4))
#print(expected_rk4[0])
#print(guess_rk4)
#for i in range(0,5):
#    print(expected_rk4[0][i]-rk4[i])
