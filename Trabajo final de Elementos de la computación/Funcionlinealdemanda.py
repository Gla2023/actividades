# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:06:58 2023

@author: glady
"""

   
import numpy as np
 
def demanda():
    """
    INPUT none
    OUTPUT Demand linear function
    type data: array
        
    Función lineal: f(x) = ax + b
    x=cantidad de producto
    f(x)= precio
    """
    a_demanda = float(input("Ingrese un número para la pendiente de la función demanda: "))
    b_demanda = float(input("Ingrese un número para la ordenada al origen de la función demanda: "))
    cantidad_producto = np.arange(1, 101) 
    demanda = a_demanda * cantidad_producto + b_demanda
    return cantidad_producto, demanda

