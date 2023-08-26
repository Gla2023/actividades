# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:49:24 2023

@author: glady
"""

peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))
icm= round(peso/(altura**2),2)
print(f"Su IMC es de:{icm}, lo cual significa: ")
if icm> 30:
    print("""Usted pertenece al rango de obesidad.""")
elif icm< 15:
    print("""Usted está en el rango de bajo peso.""")
else: print("""Usted está  en el rango normal""")
