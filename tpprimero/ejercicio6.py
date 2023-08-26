# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:14:56 2023

@author: glady
"""
print("Convertidor de monedas")
pesos_argentinos=float(input("Ingrese la cantidad de pesos argentinos que tiene:"))
dolares=float(pesos_argentinos*550.50)
reales=float(pesos_argentinos*57.76)
euros=float(pesos_argentinos*302.85)

print("Usted tiene", pesos_argentinos, "pesos argentinos, los cuales se convierten en:")
print("-", round(dolares,2), "dólares.")
print("-", round(reales,2), "reales.")
print("-", round(euros,2), "euros.")