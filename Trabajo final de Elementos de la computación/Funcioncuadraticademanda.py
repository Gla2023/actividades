# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:43:45 2023

@author: glady
"""

import numpy as np
a=0
b=0
c=0
def pedir_fc1():
    """
    INPUT none
    OUTPUT Quadratic demand function
    type data: array
        
    Quadratic demand function: f(x) = axx + bx + c
    x=cantidad de producto
    f(x)= precio
    """
    a = float(input("Ingrese un número para la pendiente de la función demanda: "))
    b = float(input("Ingrese un número para la ordenada al origen de la función demanda: "))
    c = float(input("Ingrese un número para la pendiente de la función demanda: "))
    cantidad_producto = np.arange(1, 101) 

    
    fc1= a * cantidad_producto* cantidad_producto + b*cantidad_producto + c 
            
    return cantidad_producto, fc1
