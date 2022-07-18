# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:24:23 2022

@author: Fernando
"""
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt 
from IPython.display import display
from numpy.polynomial.chebyshev import chebfit

class Interpolation:
    def Interpol(self,a):
        x_data = []
        y_data = []
        for i in a: 
            x_data.append(i[0])
            y_data.append(i[1])
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        p = lagrange(x_data, y_data)
        p1 = chebfit(x_data, y_data, 10)
        print(p)
        return p, p1


        
        