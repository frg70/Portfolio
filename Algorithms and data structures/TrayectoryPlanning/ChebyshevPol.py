# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:24:23 2022

@author: Fernando
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d, interp2d
from sympy.abc import x, y
from sympy import lambdify

class Interpolation:
    def Interpol(self,a):
        x_data = []
        y_data = []
        for i in a: 
            x_data.append(i[0])
            y_data.append(i[1])
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        interpx = interp1d(x_data, y_data, 'cubic')
        plt.plot(x_data, interpx)
        plt.show()
        return 




        
        