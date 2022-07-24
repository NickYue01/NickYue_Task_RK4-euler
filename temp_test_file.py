# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:14:49 2022

@author: nicko
"""

import numpy as np
t = np.linspace(0,10,11)
for i in range(0,0):
    print(i)
z = []
x = np.array([1.0, 0.01])
y = np.array([1.5, 0.05])
z.append(x)
z.append(y)
z = np.array(z)
print(type(z))
print(z.T[1])
#print(z.T)
