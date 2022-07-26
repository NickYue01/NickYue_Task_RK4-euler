# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:31:03 2022

@author: nicko
"""


import numpy as np
import matplotlib.pyplot as plt
import math
from odesolve import solveto,rk4


def f(x, t):
    return x 
#I'm not familiar with how to produce points/dec. So I just list 10 evenlt distributed value from 0 to 1 in log form.
x_base = [0.1,0.1258925,0.1584893,0.1995262,0.2511886,0.3162278,0.3981072,0.5011872,0.6309572,0.7943282,1]
h = []

#5 loops for 5 decs. 
for i in range(1,6):
    my_list = []
    #for every element in the x_base array, times the corresponding 10's power
    for j in x_base:
        my_list.append(j*10**(-6+i))
    #turn the lsit into array, and conbine the arrays.
    my_list =np.array(my_list)
    h = np.concatenate((h,my_list))

#real value for x(1)
xtrue = math.exp(1)
#empty array used for store the caculated estimated values
my_diff_E = []
my_diff_rk4 =[]
for i in h:
    xguess_E = solveto(f, 1, 0, 1, i)
    xguess_rk4 = solveto(f, 1, 0, 1, i,rk4)
    #print(xguess)
    difference_E = abs(xguess_E - xtrue) 
    difference_rk4 = abs(xguess_rk4 - xtrue) 
    my_diff_E.append(difference_E)
    my_diff_rk4.append(difference_rk4)
my_diff_E=np.array(my_diff_E)
my_diff_rk4=np.array(my_diff_rk4)

#plot the diagram. 
plt.figure(figsize=(16,12),dpi = 80)
plt.plot(h,my_diff_E,'ro',label='euler')
plt.plot(h,my_diff_rk4,'bo',label = 'rk4')
plt.xlabel('h',fontsize=35)
plt.ylabel('error',fontsize=35)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#set the axis in log form
plt.xscale('log')
plt.yscale('log')
plt.legend(loc ='lower right',fontsize=20)
plt.savefig('error.jpg')
plt.show()

