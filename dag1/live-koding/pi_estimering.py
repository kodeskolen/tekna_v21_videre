# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:46:03 2021

@author: Marie
"""

from pylab import *
import pylab as pl

pl.plot()

def kast_dart():
    """Kast en tilfeldig dart
    returnerer koordinatene 
    til kastet.
    x og y skal  være mellom -1 og 
    1 """
    
    x_koordinat = uniform(-1, 1)
    y_koordinat = uniform(-1, 1)
    return x_koordinat, y_koordinat

def pytagoras(katet1, katet2):
    """Tar inn katetene i rettvinklet trekant.
    returnerer hypotenusen"""
    return sqrt(katet1**2 + katet2**2)

def traff_blinken(dart_x, dart_y):
    """Tar inn koordinater.
    returerer True dersom treff
    False hvis ikke."""
    avstand_origo = pytagoras(dart_x, dart_y)
    
    return avstand_origo < 1

dart_x, dart_y = kast_dart()
print(dart_x, dart_y)
print(traff_blinken(dart_x, dart_y))
    
antall_kast = 1000
antall_treff = 0

dart_traff_x = zeros(antall_kast)+3
dart_traff_y = zeros(antall_kast)+3

dart_bommet_x = zeros(antall_kast)+3
dart_bommet_y = zeros(antall_kast)+3



for kast in range(antall_kast):
    dart_x, dart_y = kast_dart()
    if traff_blinken(dart_x, dart_y):
        dart_traff_x[kast] = dart_x
        dart_traff_y[kast] = dart_y
        antall_treff += 1
    else:
        dart_bommet_x[kast] = dart_x
        dart_bommet_y[kast] = dart_y
    
    plot(dart_traff_x, dart_traff_y, "gx")
    plot(dart_bommet_x, dart_bommet_y, "rx")
    xlim(-1, 1)
    ylim(-1, 1)
    pause(0.2)
    

estimert_sannsynlighet = antall_treff/antall_kast

estimert_pi = 4*estimert_sannsynlighet
 print(f"Antall kast: {antall_kast}")
print(f"Antall treff: {antall_treff}")
print(f"Estimert sannsynlighet: {estimert_sannsynlighet}")
print(f"Esimert pi: {estimert_pi}")


    
    