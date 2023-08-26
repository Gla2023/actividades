# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 21:10:54 2023

@author: glady
"""

def largest_palindrome():
    largest = 0
    
    for i in range(999999, 100000, -1):
        if str(i) == str(i)[::-1]:  # Verificar si es palindrómico
            largest = i
            break
    
    return largest

# Llamada a la función
result = largest_palindrome()
print("El mayor número palindrómico de seis dígitos es:", result)