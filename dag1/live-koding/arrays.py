# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:25:24 2021

@author: Marie
"""

from pylab import arange, linspace, zeros

x = arange(0, 10, 0.5)
print(x)
y = linspace(0, 9.5, 20)
print(y)
z = zeros(10)
print(z)
z[0] = 10
print(z)
print(x[19])