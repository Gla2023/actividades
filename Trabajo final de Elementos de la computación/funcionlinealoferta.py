# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:41:38 2023

@author: glady
"""

import numpy as np
a=0
b=0
def pedir_fl2():
    """
    INPUT none
    OUTPUT Linear function offer
    type data array
        
    Función lineal: f(x) = ax + b
    x=cantidad de producto
    f(x)= precio
    """
    a = float(input("Ingrese un número para la pendiente de la función oferta: "))
    b = float(input("Ingrese un número para la ordenada al origen de la función oferta: "))
    cantidad_producto = np.arange(1, 101) 

    
    fl2= a * cantidad_producto+b 
            
    return cantidad_producto, fl2

