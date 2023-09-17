# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:31:48 2023

@author: glady
"""
import funcionlinealoferta
import Funcionlinealdemanda
import Funcioncuadraticademanda
import Funcioncuadraticaoferta
import Excesodedemanda                                                                                                                                                                                                                                                                                                                                                                                                                         
import Excesooferta
import Graficofertademanda2
import Graficoofertademanda

def main():
    print("Vamos a modelizar la oferta y la demanda")
    Eleccion = input("Elige una opción:\n"
                     "l para función lineal\n"
                     "c para función cuadrática\n"
                     ":......")

    if Eleccion == "l":
        
        fl1 = Funcionlinealdemanda.pedir_fl1()
        fl2 = funcionlinealoferta.pedir_fl2()
        
        
        return fl1, fl2, Graficoofertademanda
    elif Eleccion == "c":
       
        fc1 = Funcioncuadraticaoferta.pedir_fc1()
       
        fc2 = Funcioncuadraticademanda.pedir_fc2()
        return fc1, fc2, Graficofertademanda2
    else:
        print("Elección inválida")
        return None

if __name__ == "__main__":
    result = main()
    print(result)




