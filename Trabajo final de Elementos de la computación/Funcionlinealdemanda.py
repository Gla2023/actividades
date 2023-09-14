# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:06:58 2023

@author: glady
"""
import numpy as np
a=0
b=0
def pedir_fl1():
    """
    INPUT none
    OUTPUT Demand linear function
    type data: array
        
    Función lineal: f(x) = ax + b
    x=cantidad de producto
    f(x)= precio
    """
    a = float(input("Ingrese un número para la pendiente de la función demanda: "))
    b = float(input("Ingrese un número para la ordenada al origen de la función demanda: "))
    cantidad_producto = np.arange(1, 101) 
    fl1= a * cantidad_producto+b 
            
    return cantidad_producto, fl1






