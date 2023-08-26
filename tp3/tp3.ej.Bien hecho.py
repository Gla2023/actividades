# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 10:18:30 2023

@author: glady
"""
presentes=0
ausentes=0
aprobados=0
desaprobados=0
suma=0
N=int(input("Ingrese la cantidad de alumnos: "))
for estudiante in range (N):
    nota=int(input(f"Ingrese la calificación del estudiante{estudiante+1}"))
    if nota!=99:
        presentes=presentes+1
        suma=suma + nota
        if nota>=4:
            aprobados = aprobados+1
        else: 
            desaprobados=desaprobados+1
    else: 
        ausentes=ausentes+1
promedio= suma/presentes
if presentes > 0:
    print(f"El promedio de calificaciones es {round(promedio,2)}")
    print(f"%Aprobados: {round(aprobados/N, 2*100)} %")
    print(f"%Desaprobados: {round(desaprobados/N*100)} %")
    print(f"%Ausentes:{round(ausentes/N*100, 2)%}")
else:
    print("No vino nadie")
    
    
    