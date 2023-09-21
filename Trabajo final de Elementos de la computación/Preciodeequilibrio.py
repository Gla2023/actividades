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
        
    Interseccion: fl1 = fl2
    """
    cantidad_producto,oferta = funcionlinealoferta.oferta()
    cantidad_producto, demanda = Funcionlinealdemanda.demanda()
   
    for i in range(len(cantidad_producto)):
        if demanda[i] == oferta[i]:
            punto_equilibrio = (cantidad_producto[i], demanda[i])
            break
    return punto_equilibrio
  
    
    
# decision=input("Quiere ver el grafico ingrese Y or N")
# if decision=="Y":
#     Graficoofertademanda()   
# else:
#     print("Gracias por usar la aplicacion")      
    