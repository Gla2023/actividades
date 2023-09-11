# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:06:58 2023

@author: glady
"""

def funcion_lineal(x, a, b):
    """
    Función lineal: f(x) = ax + b
    """
    return a * x + b

# Ejemplo de uso:
a = 2
b = 3
x = 5
resultado = funcion_lineal(x, a, b)
print(f"El resultado de la función lineal f({x}) = {a}x + {b} es: {resultado}") 
