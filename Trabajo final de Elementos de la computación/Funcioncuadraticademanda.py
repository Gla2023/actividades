# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:43:45 2023

@author: glady
"""

import numpy as np
a=0
b=0
c=0
def pedir_fc1(a, b, c):
    """
    INPUT none
    OUTPUT Función demanda
    type data float
        
    Función lineal: f(x) = ax + b
    """
    x = np.arange(1, 101) 

    
    fc1= a * x* x + b*x + c 
            
    return fc1