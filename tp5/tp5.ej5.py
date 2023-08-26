# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:40:37 2023

@author: glady
"""

def suma_divisores(a):
    """
    Parameter a:
    type: int
    description: number

    Returns
    type: int
    description: suma de los divisores del parametro.

    """
    suma_divisores=1
    for numero in range (2, a):
        resto=a%numero
        if resto==0:
            suma_divisores+=numero
    return suma_divisores

def son_amigos(a,b):
   if suma_divisores(a)==b and suma_divisores(b)==a:
            print ("Los numeros son amigos")
   else: print ("Los numeros no son amigos")
   
son_amigos(220, 284)

        
