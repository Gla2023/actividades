# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:05:18 2023

@author: glady
"""
factorial=1
numero=int(input("Ingrese un número para obtener su factorial: "))
for i in range(1, numero+1):
    factorial*=i
print (f"El factorial es igual a {factorial}")