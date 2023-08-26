# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:10:35 2023

@author: glady
"""

print("Ejercicio 9 tp 3")

numero=int(input("Ingrese un número: "))
for i in range(2, numero):
    resto=numero%i
    contador=0    
    if resto==0:
        
        contador=+1
if contador==0:
    print ("El numero es primo")
else: print("El número es compuesto")
    

        
        
    
    
