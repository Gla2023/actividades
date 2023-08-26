# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:44:46 2023

@author: glady
"""

print("Convertidor de temperaturas")
temperatura_celcius=float(input("Ingrese la temperatura en grados Celcius:"))
temperatura_fahrenheit= (temperatura_celcius*9/5)+32
temperatura__kelvin= temperatura_celcius+273.15
print("La temperatura en Fahrenheit es de:", temperatura_fahrenheit)
print("La temperatura en Kelvin es de:", temperatura__kelvin)