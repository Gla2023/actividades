# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 19:29:07 2023

@author: glady
"""
divisor:1
suma=0

numero=int(input("Ingrese un número para saber si es triperfecto: "))

for divisor in range (1, numero+1):
    resto=int(numero%divisor)
    if resto==0:
        suma+=divisor
if suma==3*numero:
        print(f"El número {numero} es triperfecto.")
else: print("El número no es triperfecto.")