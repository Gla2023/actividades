# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:33:41 2023

@author: glady
"""

def precio_equilibrio():
    """
    INPUT none
    OUTPUT precio de equilibrio de las funciones oferta y demanda ingresadas.
    type data float
        
    Interseccion: fc1=FC2
    """
    import Funcioncuadraticaoferta
    import Funcioncuadraticademanda
    import Graficoofertademanda2
    cantidad_producto, fc2 = Funcioncuadraticaoferta.pedir_fc2()
    cantidad_producto, fc1 = Funcioncuadraticademanda.pedir_fc1()

    for cantidad_producto in fc1:
        if cantidad_producto in fc2:
            equilibrio_producto= [cantidad_producto]
            equilibrio_precio=fc1[equilibrio_producto]
            print(f"La interseccion entre las funciones es:{equilibrio_producto}, {equilibrio_precio}")
        decision=input("Quiere ver el grafico ingrese Y or N")
        if decision=="Y":
            Graficoofertademanda2()   
        else:
            print("Gracias por usar la aplicacion")  
    