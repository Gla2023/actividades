# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 11:23:22 2023

@author: glady
"""

# print("Calculo del perímetro de un rectángulo")
# base=float(input("Ingrese el valor de la base del rectángulo:"))
# altura=float(input("Ingrese el valor de la altura del rectángulo:"))
# perimetro = 2*base+2*altura
# print(f"El resultado del perímetro es: {perimetro}")

# print("Promedio de notas")
# nota1=float(input("Ingrese la nota del primer parcial:"))
# nota2=float(input("Ingrese la nota del segundo parcial:"))
# promedio=(nota1+nota2)/2
# print(f"El promedio es {promedio}")

operacion=input("Ingrese una operación o salir: ")
while operacion!= "salir":
    numero1=float(input("Ingrese un número:"))
    numero2=float(input("Ingrese otro número:"))
    if operacion.lower()=="+":
        resultado=numero1+numero2
    elif operacion=="-":
        resultado=numero1-numero2
    elif operacion=="*":
        resultado=numero1*numero2
    elif operacion=="/":
         if numero2!=0:
             resultado=numero1/numero2
         else: print("No se puede dividir por cero")
    else: print("La operación elegida no es válida")
    print(f"{numero1}{operacion}{numero2}={resultado}")
    operacion=input("Ingrese una operación o salir: ")
print("Gracias por usar la calculadora")    
    
