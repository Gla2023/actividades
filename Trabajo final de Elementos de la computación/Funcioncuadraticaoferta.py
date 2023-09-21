# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:45:02 2023

@author: glady
"""

import numpy as np
a=0
b=0
c=0
def pedir_fc2():
    """
    INPUT none
    OUTPUT quadratic function offer
    type data: array
        
    Función cuadrática: f(x) = axx + bx+c
    x=cantidad de producto
    f(x)= precio
    """
    a = float(input("Ingrese un número para el coeficiente cuadrático función oferta: "))
    b = float(input("Ingrese un número para el coeficiente lineal de la función oferta: "))
    c = float(input("Ingrese un número para el coeficiente independiente de la función oferta: "))
    cantidad_producto = np.arange(1, 101)
 
    fc2= a * cantidad_producto* cantidad_producto + b*cantidad_producto + c 
            
    return cantidad_producto, fc2
