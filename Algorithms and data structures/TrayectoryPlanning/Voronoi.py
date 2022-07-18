# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:31:37 2022

@author: Fernando
"""

from foronoi import Voronoi, Polygon, Visualizer, VoronoiObserver
import foronoi
import re 


class Voro:
    def VoronoiPoly(self,points):
        # Definimos nuestros puntos

# Definimos nuestro polígono que encierra a los puntos
        polygon = Polygon([(2.5, 10),(5, 10),(10, 5),(10, 2.5),(5, 0),(2.5, 0),(0, 2.5),(0, 5),])
    
        # Iniciamos el algoritmo
        v = Voronoi(points)
    
    #Agregamos la visualización de la creación de los diagramas
        v.attach_observer(VoronoiObserver())
    
    # Creamos el diagrama
        v.create_diagram(points=points)
    # Estas solo son algunas propiedades
        edges = v.edges
        vertices = v.vertices
        arcs = v.arcs
    #points = v.points
    #Ploteamos nuestras gráficas y las visualizamos
        foronoi.Visualizer(v).plot_sites().plot_edges(show_labels=False).plot_vertices().show()
        return 
    
