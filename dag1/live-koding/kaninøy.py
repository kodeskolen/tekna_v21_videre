# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:25:06 2021

@author: Marie
"""

from pylab import zeros, plot, show, xlabel, ylabel, title

antall_år = 100

fødselsrate = 0.2
dødsrate = 0.1
vekstrate = fødselsrate - dødsrate

k = zeros(antall_år)
k[0] = 200
for t in range(1, antall_år):
    k[t] = k[t-1] + vekstrate*k[t-1]
    
print(k)
plot(k, "-o")
xlabel("Tid [år]")
ylabel("Antall kaniner")
title("Simularing av befolkning på Kaninøya")
show()
