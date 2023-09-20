# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:41:38 2023

@author: glady
"""

import numpy as np

def oferta():
  """
    INPUT none
    OUTPUT Linear function offer
    type data array
        
    Función lineal: f(x) = ax + b
    x=cantidad de producto
    f(x)= precio
  """  
  a_oferta = float(input("Ingrese un número para la pendiente de la función oferta: "))                                                                                                                                                 
  b_oferta = float(input("Ingrese un número para la ordenada al origen de la función oferta: "))
  cantidad_producto = np.arange(1, 101) 
  oferta = a_oferta * cantidad_producto + b_oferta
  return cantidad_producto, oferta



