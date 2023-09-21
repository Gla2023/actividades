# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:33:41 2023

@author: glady
"""
import Funcioncuadraticaoferta
import Funcioncuadraticademanda

def precio_equilibrio():
    """
    INPUT none
    OUTPUT precio de equilibrio de las funciones oferta y demanda ingresadas.
    type data float
        
    Interseccion: fc1=FC2
    """
    cantidad_producto, fc2 = Funcioncuadraticaoferta.pedir_fc2()
    cantidad_producto, fc1 = Funcioncuadraticademanda.pedir_fc1()

    for i in range(len(cantidad_producto)):
        if fc2[i] == fc1[i]:           
            equilibrio_producto= (cantidad_producto[i], fc1[i])
            print(f"La interseccion entre las funciones es:{equilibrio_producto}")
        # decision=input("Quiere ver el grafico ingrese Y or N")
        # if decision=="Y":
        #     Graficoofertademanda2()   
        # else:
          
          
                   
               
          