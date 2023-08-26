# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 19:23:11 2023

@author: glady
"""
i=1
N=int(input("Ingrese un número natural: "))
for i in range(i, N):
    if N%i==0:
        print(f"El número {i} es divisor natural de {N}")