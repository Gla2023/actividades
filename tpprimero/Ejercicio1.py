# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:54:21 2023

@author: glady
"""
#ejercicio1#
print("Vamos a calcular el perímetro de un rectángulo")

def calcular_perimetro(base, altura):
    perimetro = 2*base + 2*altura
    return perimetro

base = float(input("Escribe el valor de la base:"))
altura = float(input("Escribe el valor de la altura:"))

resultado_perimetro = calcular_perimetro(base, altura)
print("El perimetro de ese rectángulo es:", resultado_perimetro)


