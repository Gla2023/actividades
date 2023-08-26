# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:38:34 2023

@author: glady
"""

print("Calculadora de IMC(Índice de masa corporal)")
peso_corporal=float(input("Ingrese su peso en kilogramos:"))
altura=float(input("Ingrese su altura en metros:"))
imc= peso_corporal/(altura**2)
print("Su IMC es:", imc)
