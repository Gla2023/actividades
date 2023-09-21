# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:07:52 2023

@author: glady
"""
import Preciodeequilibrio
from scipy.integrate import quad
def h():
    """ 
    Dieferencia entre las funciones a integrar.
    """
    punto_equilibrio = Preciodeequilibrio.precio_equilibrio().punto_equilibrio
    x_equilibrio = punto_equilibrio[0]
    f_x = punto_equilibrio[1]
    g_x = Preciodeequilibrio.Funcionlinealdemanda  # Reemplaza con la función de oferta correcta
    return f_x - g_x 

    integral_result, error = quad(h, 0, x_equilibrio)

    print("El valor de la integral de h(x)", integral_result)

 
  