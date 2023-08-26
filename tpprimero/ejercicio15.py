# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:49:04 2023

@author: glady
"""

print("Calculadora de descuentos")
precio_original=float(input("Ingrese el precio original del producto:"))
descuento=float(input("Ingrese el porcentaje de descuento:"))
precio_final=precio_original-precio_original*(descuento/100)
print("El precio final es de:", precio_final)