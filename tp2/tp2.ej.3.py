# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:40:28 2023

@author: glady
"""

numero_1=float(input("Ingrese un número: "))
numero_2=float(input("Ingrese otro número: "))
if numero_1 > numero_2:
    print(f"El primer numero, {numero_1}, es el mayor.")
elif numero_1==numero_2:
    print("Los números son iguales, intentelo nuevamente")
else:  print(f"El segundo número {numero_2} es el mayor")

