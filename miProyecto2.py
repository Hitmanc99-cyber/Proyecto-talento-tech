# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 10:01:34 2025

@author: DISTRIMEDV
"""


import pandas as pd
import numpy as np 


df_csv =pd.read_csv("Casos_positivos_de_COVID-19_en_Colombia._20251102.csv")
print(df_csv)

df = df_csv.copy()
