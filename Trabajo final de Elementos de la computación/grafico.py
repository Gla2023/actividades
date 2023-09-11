# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:00:35 2023

@author: glady
"""

import matplotlib.pyplot as plt
import numpy as np


       
a=3
b=2
x = np.arange(1, 101) 
fl1= a * x + b

plt.figure(figsize=(8, 6))
plt.plot(x, fl1, label=f'f(x) = {a}x + {b}', color='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de una función lineal')
plt.grid(True)
plt.legend()
plt.show()




