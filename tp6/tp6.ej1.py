# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:34:44 2023

@author: glady
"""

def frecuencia_caracter(cadena):
    """
    parametros: cadena tipo string
    Returns: diccionario que cuenta los caracteres
    """
    diccionario = {}
    
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
            
    return diccionario

cadena = "Gladys"
resultado = frecuencia_caracter(cadena)
print(resultado)
