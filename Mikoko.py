"""
importing the excel Sheet
we use the panda module to read the excel file

we use the read_excel() to read the data into a pandas Data Frame

we use df to represent Data Frame

"""

#import pysco

#from request import PandaRequest
import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#import the mikoko csv file and the new savedrecs  text file
file = r'Mikoko.csv'
ftext = r'savedrecs.txt'
df = pd.read_csv(file)
dataf = pd.read_fwf(ftext)

#or dataf = pd.read_csv(ftext, delimiter = '\t', index_col = False)
#print(df)

print('Max', df['TotalCitations'].max())
print('Min', df['TotalCitations'].min())

#identify if the files are present
print(df)
print(dataf)

#print('Max', dataf['Z9'].max())
"""

#psyco.full()

df = pd.read_excel('Mikoko.xlsx', sheetname = 'MIkoko')

print("Column heading")

#the list of columns will becalled df.columns

print(df.columns)

#create a single list of a column

print(df['Title'])

#use a loop to iterate over the list

for i in df.index:
    print(df['Title'][i])

#we save an entire column into a list
listTitle = df['Title']

print(listTitle[0])
"""
