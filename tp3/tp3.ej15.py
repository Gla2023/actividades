# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 19:27:57 2023

@author: glady
"""
while encuestados!=120:
consumidores=input("Ingrese los números 1, 2, 3 para la marca elegida por el consumidor.")
encuestados=+1
for consumidores in range (120):
    if consumidores==1:
        marca1=+1
    elif consumidores==2:
        marca2=+1 
    else: marca3=+1
if marca1>marca2 and marca2 >marca3:
    marca_más_elegida=marca1
elif marca2>marca1 and marca1 >marca3:
    marca_más_elegida= marca2
else: marca_más_elegida=marca3
print(f"La marca más elegida es {marca_más_elegida}")