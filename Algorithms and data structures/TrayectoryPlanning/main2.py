# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:26:07 2022

@author: Fernando
"""

import pygame
import math 
from RRTree import RRTMap
from RRTree import RRTGraph
from Interpolation import Interpolation
from MultipleRoots import RootsPolynomial
import matplotlib.pyplot as plt
import numpy as np 
from sympy.abc import x 
from numpy.polynomial import Polynomial
from Voronoi import Voro
def main():
    dimensions = (600,1000)
    start =(50,50)
    goal = (510,510)
    obsdim = 30
    obsnum = 50
    iteration = 0
    
    Inter = Interpolation()
    Roots = RootsPolynomial()
    Vor = Voro()
    pygame.init()
    map=RRTMap(start,goal,dimensions,obsdim,obsnum)
    graph = RRTGraph(start,goal,dimensions,obsdim, obsnum)


    obstacles = graph.makeobs()
    map.drawMap(obstacles)
    
    
    while(not graph.path_to_goal()):
        if iteration % 10 ==0:
            X,Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)
        else: 
            X,Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2,0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)
        if iteration % 5 == 0: 
                pygame.display.update()
        iteration +=1
    a = graph.getPathCoords()
    map.drawPath(a)
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)
    x_data = []
    y_data = []
    for i in a: 
        x_data.append(i[0])
        y_data.append(i[1])
    x_data = np.array(x_data)
    y_data = np.array(y_data)
    Inter = Interpolation()
    f = Inter.Interpol(a)
    coef = Polynomial(f[0].coef[::-1]).coef
    roots = Roots.coefficients(coef)
    print(roots)
    #Vor.VoronoiPoly(roots)
    #Root = Roots.Roots(-1, f[0], 0.0001) 
    

            
    


if __name__ == "__main__":
    main() 