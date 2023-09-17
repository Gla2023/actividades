# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:33:03 2023

@author: glady
"""

import Funcioncuadraticaoferta
import Funcioncuadraticademanda
import matplotlib.pyplot as plt

def graficar_oferta_demanda2():
    """
    INPUT none
    OUTPUT Supply and demand graph
    type graph
        
    """
    cantidad_producto, fc2 = Funcioncuadraticaoferta.pedir_fc2()
    cantidad_producto, fc1 = Funcioncuadraticademanda.pedir_fc1()

    # Graficar la función de oferta
    plt.plot(cantidad_producto, fc2, label="Oferta")

    # Graficar la función de demanda
    plt.plot(cantidad_producto, fc1, label="Demanda")

    # Personalizar la gráfica
    plt.xlabel("Cantidad de Producto")
    plt.ylabel("Precio")
    plt.title("Funciones de Oferta y Demanda")
    plt.legend()

    # Mostrar la gráfica
    plt.show()

# Llama a la función para graficar oferta y demanda
graficar_oferta_demanda2()