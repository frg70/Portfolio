# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:47:04 2022

@author: Fernando
"""

import numpy as np 
from sympy.abc import x,y,z

class RootsPolynomial:
    def NR(self,x0,f,tol):
        error = 0
        fprime = f.diff(x)
        fprimeprime = f.diff(x)
        while error > tol:
            xr = x0 - (f.subs(x,x0)*fprime.subs(x,x0))/(fprime.subs(x,x0)**2 - (f.subs(x,x0)*fprimeprime.subs(x,x0)))
            x0 = xr
            error = abs(xr-x0)
        print('La raíz está en: ', xr)
        return 
    def coefficients(self,coef):
        roots = np.roots(coef)
        return roots