# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:41:38 2023

@author: glady
"""

import numpy as np
a=0
b=0
def pedir_fl2(a, b):
    """
    INPUT none
    OUTPUT Función demanda
    type data float
        
    Función lineal: f(x) = ax + b
    """
    x = np.arange(1, 101) 

    
    fl2= a * x+b 
            
    return fl2