# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:42:09 2023

@author: glady
"""

numero_n=float(input("Ingrese un número n:"))
if numero_n % 5== 0 and numero_n % 3== 0:
    print(f"{numero_n} es múltiplo de 5 y 3")
elif numero_n % 3== 0:
    print( f"{numero_n} es múltiplo de 3")
elif numero_n % 5== 0:
    print(f"{numero_n} es mútiplo de 5")
else: print(f"{numero_n} no es mútiplo ni de 5 ni de 3")