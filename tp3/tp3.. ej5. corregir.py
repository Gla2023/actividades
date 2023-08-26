# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:47:15 2023

@author: glady
"""

print("Promedio de las calificaciones del parcial de Introducción a la Programación")
total_alumnos=0
alumnos_ausentes=0
alumnos_aprobados=0
calificacion_alumno=input("Ingrese la calificación del alumno o Fin:")
while calificacion_alumno!="Fin":
    calificacion_alumno=float(calificacion_alumno)
    calificacion_totales=+calificacion_alumno
    if calificacion_totales!=0 and calificacion_alumno> 4:
        alumnos_aprobados=+1
    elif calificacion_alumno!=0 and calificacion_alumno=="99":
        alumnos_ausentes+=1
    else: calificacion_alumno!=0 and calificacion_alumno<4
    alumnos_desaprobados=+1
    total_alumnos=alumnos_aprobados+alumnos_ausentes+alumnos_desaprobados
    promedio= calificacion_totales/total_alumnos
    porcentaje_aprobados= alumnos_aprobados/total_alumnos*100
    porcentaje_desaprobados= alumnos_desaprobados/total_alumnos*100
    porcentaje_ausentes= alumnos_ausentes/total_alumnos*100
    calificacion_alumno=input("Ingrese la calificación del alumno o Fin:")
       
print(f"El promedio de las notas de los estudiantes fue de {promedio}. El porcentaje de aprobados fue de {porcentaje_aprobados}. El porcentaje de desaprobados fue de {porcentaje_desaprobados} y el porcentaje de ausentes fue de {porcentaje_ausentes}")