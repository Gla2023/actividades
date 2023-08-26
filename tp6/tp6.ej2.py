# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 10:25:13 2023

@author: glady
"""

def depuracion_de_listas(lista):
    lista=lista()
    lista_nueva=lista_nueva()
    for i in lista():
        if i not in lista_nueva:
            lista_nueva=lista_nueva.append(i)
    return lista_nueva()

def test_de_funcion():
    print("Testeando la funcion")
    assert(depuracion_de_listas())
    print("pasa")
    
def main():
    
    test_de_funcion()
main()

