
"""
@author: Nishant
"""

import pandas as pd
import numpy as np
import xlrd

csv1 = pd.read_excel('animax.xlsx', 'anime', index_col=None)
csv1.to_csv('csvfile1.csv', encoding='utf-8',index = False)

csv2 = pd.read_excel('animax.xlsx', 'S1', index_col=None)
csv2.to_csv('csvfile2.csv', encoding = 'utf-8', index= False)

csv3 = pd.read_excel('animax.xlsx','S2',index_col=None)
csv3.to_csv('csvfile3.csv',encoding = 'utf-8', index=False)

csv4 = pd.read_excel('animax.xlsx','S3', index_col = None)
csv4.to_csv('csvfile4.csv',encoding= 'utf-8', index = False)

csv5 = pd.read_excel('animax.xlsx', 'S4', index_col=None)
csv5.to_csv('csvfile5.csv', encoding='utf-8',index = False)

csv6 = pd.read_excel('animax.xlsx', 'S5', index_col=None)
csv6.to_csv('csvfile6.csv', encoding = 'utf-8', index= False)

csv7 = pd.read_excel('animax.xlsx','S6',index_col=None)
csv7.to_csv('csvfile7.csv',encoding = 'utf-8', index=False)

csv8 = pd.read_excel('animax.xlsx','S7', index_col = None)
csv8.to_csv('csvfile8.csv',encoding= 'utf-8', index = False)

csv9 = pd.read_excel('animax.xlsx','S8',index_col=None)
csv9.to_csv('csvfile9.csv',encoding = 'utf-8', index=False)

csv10 = pd.read_excel('animax.xlsx','S9', index_col = None)
csv10.to_csv('csvfile10.csv',encoding= 'utf-8', index = False)
