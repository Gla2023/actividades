# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:00:35 2023

@author: glady
"""

import matplotlib.pyplot as plt
import numpy as np
import funcionlinealoferta as flo
import Funcionlinealdemanda as fld

array=flo.pedir_fl2()
cantidad_productos=np.array_split(array, 100)
array2=fld.pedir_fl1()
plt.plot(flo.pedir_fl2( ), [flo(i) for i in flo.pedir_fl2()])
plt.plot(fld.pedir_fl1, [fld(i) for i in fld.pedir_fl1()])
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.savefig("output.png")
plt.show()

