# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:45:58 2023

@author: glady
"""

def multiplos(n):
    n = int(input("Ingrese un numero: "))
    de_5 = []
    de_3 = []
    resto_5 = n % 5
    resto_3 = n % 3
    if resto_5 == 0:
        de_5.append(n)
    elif resto_3 == 0:
        de_3.append(n)
    
    if not de_5 and not de_3:
        return f"El numero {n} no es multiplo de 5 ni de 3"
    return de_5, de_3

print(multiplos(4))






