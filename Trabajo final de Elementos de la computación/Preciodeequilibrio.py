# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:27:06 2023

@author: glady
"""
import funcionlinealoferta
import Funcionlinealdemanda
import Graficoofertademanda
def precio_equilibrio():
    """
    INPUT none
    OUTPUT precio de equilibrio de las funciones oferta y demanda ingresadas.
    type data float
        
    Interseccion: fl1 = fl2 or fc1=FC2
    """
   

cantidad_producto, fl2 = funcionlinealoferta.oferta()
cantidad_producto, fl1 = Funcionlinealdemanda.demanda()

for i in range(len(cantidad_producto)):
    if fl1[i] == fl2[i]:
        punto_equilibrio = (cantidad_producto[i], fl1[i])
        print("El punto de intersección entre oferta y demanda es:", punto_equilibrio)
# decision=input("Quiere ver el grafico ingrese Y or N")
# if decision=="Y":
#     Graficoofertademanda()   
# else:
#     print("Gracias por usar la aplicacion")      
    