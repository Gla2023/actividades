# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:00:35 2023

@author: glady
"""

import matplotlib.pyplot as plt
import main

plt.figure(figsize=(8, 6))
plt.plot(main.main(), label='f(x) ', color='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de una función oferta y demanda')
plt.grid(True)
plt.legend()
plt.show()




