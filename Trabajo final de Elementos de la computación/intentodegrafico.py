# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:56:07 2023

@author: glady
"""

import seaborn as sns
sns.set_theme(style="whitegrid")

# Load the example Titanic dataset
import funcionlinealoferta as flo
import funcionlinealdemanda as fld

# Set up a grid to plot survival probability against several variables
g = sns.PairGrid(flo, y_vars=flo,
                 x_vars=["class", "sex", "who", "alone"],
                 height=5, aspect=.5)
g = sns.PairGrid(fld, y_vars="survived",
                 x_vars=["class", "sex", "who", "alone"],
                 height=5, aspect=.5)

# Draw a seaborn pointplot onto each Axes
g.map(sns.pointplot, scale=1.3, errwidth=4, color="xkcd:plum")
g.set(ylim=(0, 1))
sns.despine(fig=g.fig, left=True)