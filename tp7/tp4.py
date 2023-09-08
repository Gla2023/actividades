# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:23:25 2023

@author: glady
"""

import urllib.request

url = "https://archive.ics.uci.edu/static/public/482/parking+birmingham.zip"
file_name = "parking_birmingham.zip"

urllib.request.urlretrieve(url, file_name)
print(f"Archivo '{file_name}' descargado correctamente.")
import zipfile
import os

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall('data')  # Cambia 'data' por la ruta donde deseas extraer los archivos

print("Archivos descomprimidos correctamente.")

import pandas as pd

s=pd.Series('data')
print(s)
