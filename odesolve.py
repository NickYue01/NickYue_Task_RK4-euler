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
    #formula for the euler method
    return x + (f (x , t ))*h
    pass


def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""
    #4 step of the Runge-Kutta method. 
    k1 = f(x,t)
    k2 = f(x+k1*h*0.5, t+0.5*h)
    k3 = f(x+k2*h*0.5, t+0.5*h)
    k4 = f(x+k3*h, t+h)
    #final step of the 4th Runge-Kutta
    return x + ( k1 + 2*k2 + 2*k3 + k4 ) * h/6
    pass


def solveto(f, x1, t1, t2, hmax, method=euler):         
    """Use many steps of method to get from x1,t1 to x2,t2"""
    
    #caculate the total full steps need. The steps for hmax.
    #using round() and / for division instead of //. using // may cause 1 loop less than the aimed value and become inaccurate. 
    the_loop = int(round((t2-t1)/hmax))
    #check if the stepsize is evenly divide or not. If not, the reminder will be the smaller step at the end. 
    reminder = t2 - t1 - the_loop*hmax
    
    #create variables for repeating use in the function. 
    x0 = x1
    t_middle = t1
    
    #if no loop is needed, the caculation will not be done, and x2 will have no value. 
    #to prevent x2 refered before used, when the_loop == 0, the value of x1 is directlly given to x2.
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
        #as the computer can't store accurate decimals like 0.1. Using round can solve the problem. 
        t_middle = round(t_middle,8)
    
    if reminder != 0:              
        if method == rk4:
            x2 = rk4 ( f , x0 , t2 , reminder)
        else:
            x2 = euler ( f , x0 , t2 , reminder)
     
    return x2
    pass


def odesolve(f, X0, t, hmax, method=euler):
    import numpy as np
    """Compute the solution at different values of t"""
    #the first value in t is the initial value, t0.
    t0 = t[0]
    tmax = t[-1]
    xt =[]
    
    #when the array X0 only contains 1 value, the program will report error. the value need to be extracted out
    try:
        my_try = X0[1]
    except:
        X0 = X0[0]
        
    #use for loop to caculate all the values for different t.
    for i in t:
        my_x = solveto(f,X0,t0,i,hmax,method)
        xt.append(my_x)
    #turn the list into the array.
    xt = np.array(xt)
    return xt
    pass
   