# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:09:53 2021

@author: Marie
"""

from pylab import zeros, plot, show, legend

antall_år = 10
dager_i_år = 365
antall_dager = antall_år*dager_i_år

k = zeros(antall_dager)
g = zeros(antall_dager)

f_k = 5/dager_i_år
a_g = 1.5/dager_i_år
f_g = 0.15/dager_i_år
d_g = 0.5/dager_i_år

k[0] = 5
g[0] = 2

for t in range(1, antall_dager):
    if t > 5*dager_i_år:
        f_k = 5.2/dager_i_år
        d_g = 0.3/dager_i_år
    k[t] = k[t-1] + f_k*k[t-1] - a_g*k[t-1]*g[t-1]
    g[t] = g[t-1] + f_g*g[t-1]*k[t-1] - d_g*g[t-1]
    
plot(k/(g+k), label="kaniner")
plot(g/(g+k), label="gauper")
legend()
show()


