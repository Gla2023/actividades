# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:41:14 2023

@author: glady
"""


def generador_primos():
    numero = 2
    while True:
        es_primo = True
        for i in range(2, numero):
            resto = numero % i
            if resto == 0:
                es_primo = False
                break
        if es_primo:
            print(numero)
        numero += 1
def intruccion():
    instruccion=input("Escribe 'proximo' para continuar la secuencia o 'terminar': ")
    if intruccion=="proximo": 
        True
    else: 
        False
def main():
    n=generador_primos()
    m=intruccion()
    if m==True:
        generador_primos()
    else: intruccion(Falso)
main()