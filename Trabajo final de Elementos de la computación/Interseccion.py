# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:27:06 2023

@author: glady
"""
import main

def interseccion():
    """
    INPUT none
    OUTPUT Interseccion entre funciones
    type data float
        
    Interseccion: fl1 = fl2 or fc1=FC2
    """
    mitad = len(main.main().result) // 2
    fl1 = main.main().result[:mitad]
    fl2= main.main().result[mitad:]
    for elemento in fl1:
        if elemento in fl2:
            interseccion= [elemento]
            print(f"La interseccion entre las funciones es:{interseccion}")
    