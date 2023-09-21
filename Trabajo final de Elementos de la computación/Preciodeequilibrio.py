# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:27:06 2023

@author: glady
"""
import funcionlinealoferta
import Funcionlinealdemanda

def precio_equilibrio():
    """
    INPUT none
    OUTPUT precio de equilibrio de las funciones oferta y demanda ingresadas.
    type data float
        
    Interseccion: fl1 = fl2 or fc1=FC2
    """
    cantidad_producto,oferta = funcionlinealoferta.oferta()
    cantidad_producto, demanda = Funcionlinealdemanda.demanda()
    punto_equilibrio = None  # Inicializar punto_equilibrio como None
    for i in range(len(cantidad_producto)):
        if demanda[i] == oferta[i]:
            punto_equilibrio = (cantidad_producto[i], demanda[i])
            break
    if punto_equilibrio:
        print("El punto de intersección entre oferta y demanda es:", punto_equilibrio)
        return punto_equilibrio
    else:
        print("No se encontró un punto de equilibrio")
        return None
    
# decision=input("Quiere ver el grafico ingrese Y or N")
# if decision=="Y":
#     Graficoofertademanda()   
# else:
#     print("Gracias por usar la aplicacion")      
    