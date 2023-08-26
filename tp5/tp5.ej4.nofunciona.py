# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:38:05 2023

@author: glady
"""

def pedir_intruccion():
  # ***
   # input= None#
   # output= Palabras "Terminar" o "Proximo"#
  #  post condicion: (T o P no importa si es minuscula o mayuscula)#
   # ***##
   intruccion=input("Ingrese proximo para seguir o terminar para salir del programa.")
   
   return intruccion
def generador_de_primos():
    
    # ***
     # input= None#
     # output= impresion de primos#
    #  post condicion: (T o P no importa si es minuscula o mayuscula)#
     # ***##
     numero=2
     for numeros in range(2,numero+1):
         resto=numero%numeros
         numero=+1
         if resto!=0:
             
             return numeros
def main():
    n=pedir_intruccion()
    while n=="Proximo":
     m= generador_de_primos()
     print(m)
     return m
main()