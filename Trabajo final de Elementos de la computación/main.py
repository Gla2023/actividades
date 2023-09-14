# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:31:48 2023

@author: glady
"""
import funcionlinealoferta
import Funcionlinealdemanda
import Funcioncuadraticademanda
import Funcioncuadraticaoferta

def main():
    print("Vamos a modelizar la oferta y la demanda")
    Eleccion = input("Elige una opción:\n"
                     "l para función lineal\n"
                     "c para función cuadrática\n"
                     ":......")

    if Eleccion == "l":
        
        fl1 = Funcionlinealdemanda.pedir_fl1(a, b)
        a = float(input("Ingrese un número para la pendiente de la función oferta: "))
        b = float(input("Ingrese un número para la ordenada al origen de la función oferta: "))
        fl2 = funcionlinealoferta.pedir_fl2(a, b)
        return fl1, fl2
    elif Eleccion == "c":
       )
        fc1 = Funcioncuadraticaoferta.pedir_fc1(a, b, c)
       
        fc2 = Funcioncuadraticademanda.pedir_fc2(a, b, c)
        return fc1, fc2
    else:
        print("Elección inválida")
        return None

if __name__ == "__main__":
    result = main()
    print(result)




