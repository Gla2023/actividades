# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:40:10 2023

@author: glady
"""

print("Conversión de tiempo")
minutos=int(input("Ingrese los minutos a convertir:"))
horas=minutos//60
resto=minutos%60
if minutos<60:
   horas_minutos_resultantes=minutos
else:
   minutos = 60
   horas_minutos_resultantes=1

   horas_minutos_resultantes=str(horas)+""+ "horas y"+ ""+str(resto)+ "" + "minutos"
   
print("La conversión resultante es:", horas_minutos_resultantes)
   
   