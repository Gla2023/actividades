# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:07:52 2023

@author: glady
"""

def exceso_demanda():
    """ 
    input 
    output
    type 
    """
import numpy as np
from scipy.integrate import quad

# Punto de equilibrio (supongamos que es x = 3)
x_equilibrio = 3
y_equilibrio = f(x_equilibrio) - g(x_equilibrio)

# Definir la función de diferencia h(x) = f(x) - g(x)
def h(x):
    return f(x) - g(x)

# Calcular la integral de h(x) en un intervalo [a, x_equilibrio]
a = 0  # Puedes cambiar el límite inferior según tus necesidades
integral_result, error = quad(h, a, x_equilibrio)

print("El valor de la integral de h(x) en el i")