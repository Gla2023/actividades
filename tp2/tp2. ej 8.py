# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:47:44 2023

@author: glady
"""

lado_1=float(input("Ingrese la medida de lado 1: "))
lado_2=float(input("Ingrese la medida de lado2: "))
lado_3=float(input("Ingrese la medida de lado 3: "))
if lado_1 + lado_2 == lado_3 or lado_2 + lado_3 == lado_1 or lado_1 + lado_3 == lado_2:
    print("El triángulo no se forma")
elif lado_1 + lado_2 < lado_3 or lado_2 + lado_3 < lado_1 or lado_1 + lado_3 < lado_2:
    print("El triángulo no se forma")
else: 
    if lado_1== lado_2 == lado_3:
      print ("El triángulo es equilátero.")
    elif lado_1==lado_2 or lado_1== lado_3 or lado_2 == lado_3:
      print ("El triángulo es isósceles")
    else: print("El triángulo es escaleno")