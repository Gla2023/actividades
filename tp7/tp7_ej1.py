# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 09:38:49 2023

@author: glady
"""

import numpy as np

l1=[i for i in range (3)]
l2=[j for j in range(3)]
l3=[h for h in range(3)]
    
matriz=np.array((l1, l2, l3))
matriz_2=np.array((l1, l2, l3))
suma_de_matrices=matriz+matriz_2
multiplicacion_de_matrices=matriz*matriz_2
print(suma_de_matrices)
print(multiplicacion_de_matrices)

