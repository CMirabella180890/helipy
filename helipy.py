# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:50:15 2020

@author: claum
"""
import numpy as np 
import math 
# ===================================================================
# Helicopter simplified analysis 
# ===================================================================
class helicopter(object):
    def __init__(self, W, rho, D, M_tip, a, g, B, c, k, cd, f):
        """
        A class for quick helicopter performances evaluation

        Parameters
        ----------
        W     : Float
            Aircraft gross weight in kilograms.
        rho   : Float
            Density in kilograms per cubic meters.
        D     : Float
            Rotor's diameter in meters.
        M_tip : Float
            Tip Mach number, non-dimensional.
        a     : Float
            Speed of sound.

        Other parameters
        -------
        V_tip        :  Float
            Tip speed defined by the equation --> V_tip = Omega * R [m/s]
        Omega        :  Float
            Angular speed in radians per seconds.
        S            :  Float
            Rotor's surface in square meters.
        Tc           :  Float
            Thrust coefficient. 
        w_h          :  Float
            Axial in duction in hovering.
        disk_loading : Float
            Dimensional parameter defined as --> T/S [N/m**2] 
        sigma        :  Float
            Solidity, non-dimensional.
        Qc           :  Float 
            Torque coefficient, non-dimensional.
        tc           :  Float 
            Mean angle-of-attack. 
        P_h          :  Float
            Total Power required for hovering. 
        FM           :  Float
            Figure of merit.
        pow_loading  :  Float
            Power loading [N/Watt].
        V_inf        :  Float
            Velocity range of the helicopter.
        Pi           :  Float
            Induced power [Watt].
        P0           :  Float 
            Parasite power [Watt].
        P_fus        :  Float 
            Airframe power [Watt].
        P_tot 
            Total power required.
        
        """
        self.W, self.rho, self.D, self.M_tip, self.a, self.g, self.B, self.c, self.k, self.cd, self.f = W, rho, D, M_tip, a, g, B, c, k, cd, f
        self.WG           = self.W*self.g
        self.V_tip        = self.M_tip*self.a
        self.Omega        = self.V_tip/(self.D/2)
        self.S            = math.pi*(self.D/2)**2
        self.Tc           = (self.WG)/(self.rho*self.S*(self.V_tip)**2)
        self.w_h          = ((self.WG)/(2*self.rho*self.S))**0.5
        self.disk_loading = self.WG/self.S
        self.sigma        = (self.B*self.c)/(math.pi*(self.D/2))
        self.Qc           = ((self.sigma*self.cd)/(8)) + self.k*((self.Tc**1.5)/(2**0.5))
        self.tc           = self.Tc/self.sigma
        self.P_h          = self.Qc*self.rho*(self.V_tip**3)*self.S
        self.FM           = (self.Tc**1.5)/(self.Qc*(2**0.5))
        self.pow_loading  = self.WG/self.P_h
        self.V_inf        = np.linspace(0.15,120,1000)
        self.Pi           = ((self.WG**2)/(2*self.rho*self.S))*(1/self.V_inf)
        self.P0           = ((self.sigma*self.cd)/(8))*self.rho*(self.V_tip**3)*self.S + ((self.sigma*self.cd)/(8))*self.rho*self.V_tip*self.S*4.7*(self.V_inf**2)
        self.P_fus        = 0.5*self.rho*self.S*self.f*(self.V_inf**3)
        self.P_tot        = self.Pi + self.P0 + self.P_fus
