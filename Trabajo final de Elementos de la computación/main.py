# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:31:48 2023

@author: glady
"""

print("Vamos a modelizar la oferta y la demanda")
Eleccion=float(input("Elige una opcion lineal/cuadrática: "))
import funcionlinealoferta
import Funcionlinealdemanda
import Funcioncuadraticademanda
import Funcioncuadraticaoferta

if Eleccion=="lineal":
    a=float(input("Ingrese un número para la pendiente de la función demanda: "))
    b=float(input("Ingrese un número para la ordenada al origen de la función demanda: "))
    fl1= Funcionlinealdemanda.pedir_fl1(a, b)
elif Eleccion=="cuadratica":
    a=float(input("Ingrese un número para el coeficiente cuadrático función demanda: "))
    b=float(input("Ingrese un número para el coeficiente lineal de la función demanda: "))
    c=float(input("Ingrese un número para el coeficiente independiente de la función demanda: "))
    fl2=funcionlinealoferta.pedir_fl2(a, b)
else: print("Elección inválida")