# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:04:55 2023

@author: glady
"""
def pedir_numero():
   numero=int(input("Ingrese un número para obtener su factorial: "))
   while numero<0:
       print("El numero ingresado no es valido.")
       numero=int(input("Ingrese otro número para obtener su factorial: "))
   return numero

def calcular_factorial(numero):
   factorial=1
   for i in range(1, numero+1):
           factorial*=i
   return factorial
def resultado_factorial():
    n=pedir_numero()
    m=calcular_factorial(n)
    print(m)
resultado_factorial()       