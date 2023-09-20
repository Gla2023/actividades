# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:56:07 2023

@author: glady
"""
import funcionlinealoferta
import Funcionlinealdemanda
import matplotlib.pyplot as plt

def graficar_oferta_demanda():
    """
    INPUT none
    OUTPUT Supply and demand graph
    type graph
        
    """
    cantidad_producto, fl2 = funcionlinealoferta.oferta()
    cantidad_producto, fl1 = Funcionlinealdemanda.demanda()

    # Graficar la función de oferta
    plt.plot(cantidad_producto, fl2, label="Oferta")

    # Graficar la función de demanda
    plt.plot(cantidad_producto, fl1, label="Demanda")

    # Personalizar la gráfica
    plt.xlabel("Cantidad de Producto")
    plt.ylabel("Precio")
    plt.title("Funciones de Oferta y Demanda")
    plt.legend()

    # Mostrar la gráfica
    plt.show()

# Llama a la función para graficar oferta y demanda
graficar_oferta_demanda()