# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 08:34:51 2020

@author: claum
"""
import numpy as np
from helipy import helicopter
import matplotlib.pyplot as plt
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
# ===================================================================
# Parameters - Sea Level Standard Day
# ===================================================================
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Data: EUROCOPTER AS 365N
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
g     = 9.81                  # Gravity acceleration [m/s**2]
h     = 0                     # Flight level in meters
rho   = 1.225                 # Density [kg/m**3]
T     = 288.16                # Temperature [K°]
p     = 1.01325E+5            # Pressure [Pascal]
a     = 343                   # Speed of sound [m/s]
D     = 11.9                  # Rotor's diameter [m]
W     = 2600                  # Gross mass [kg]
M_tip = 0.7                   # Reference tip Mach number
k     = 1.15                  # Statistical factor inside the helicopter polar
cd    = 0.01                  # Mean drag coefficient
B     = 4                     # Number of blades
c     = 0.385                 # Chord (costant over all the blade's radius)
f     = 0.007                 # Airframe equivalent wetted surface
mc    = np.zeros(1000)        # Preparing a vector 
max_continous = 3.88E+5       # Max continous power for the chosen helicopter
for i in range(len(mc)):      # Max continous for plot 
    mc[i]    = max_continous
# ===================================================================
# Parameters - Sea Level Standard Day
# =================================================================== 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
# ===================================================================
# Starting analysis with class helicopters
# =================================================================== 
my_helicopter = helicopter(W, rho, D, M_tip, a, g, B, c, k, cd, f)
# ===================================================================
# Plotting results of Power breakdown
# =================================================================== 
fig1 = plt.figure()
plt.plot(my_helicopter.V_inf, my_helicopter.Pi/1000)
plt.plot(my_helicopter.V_inf, my_helicopter.P0/1000)
plt.plot(my_helicopter.V_inf, my_helicopter.P_fus/1000)
plt.plot(my_helicopter.V_inf, my_helicopter.P_tot/1000)
plt.plot(my_helicopter.V_inf, mc/1000, linestyle='-.', linewidth=2)
plt.xlabel('$V_{\infty} \,\, [m/s]$')              # x-label to the axes.
plt.ylabel(r'Power - $P \times 1000 \,\, [W]$')     # y-label to the axes.
plt.title(r'Power breakdown')    # Title to the axes.
plt.ylim(0, 0.6E+3)
plt.xlim(0, 120)
plt.grid(True, linestyle='-.')
plt.show()    