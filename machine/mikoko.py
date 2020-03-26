"""
importing the excel Sheet
we use the panda module to read the excel file

we use the read_excel() to read the data into a pandas Data Frame

we use df to represent Data Frame

"""

#import psyco  if need be
#from request import PandaRequest
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import numpy as npy
import pandas as pds

#import the mikoko csv file to analyze and wrangle the data
#file = r'Mikoko1.csv
#df = pds.read_csv(file) or use

dfile = pds.read_csv('Mikoko1.csv')


# or use ftext = r'savedrecs.txt'
#to read a text file
#dataf = pd.read_fwf(ftext)
#or dataf = pd.read_csv(ftext, delimiter = '\t', index_col = False)

#print(dfile) #test the if the file is loaded

#print('Max', dfile['Volume'].max())
#print('Min', dfile['TotalCitations'].min())

#identify if the files are present
#print(dfile)

#check the column headers
#print(dfile.columns)

#psyco.full()
#check the data for any error one column at a time

#print(dfile['Title'])
#create a loop to iterate over the list

"""for i in dfile.index:
    print(dfile['Titles'][i])"""

#listTitle = dfile['Title']

#print(listTitle[0])


y = dfile['1990']
x = dfile['TotalCitations']

#print(x,y)
#y1 = npy.cos(x)

plt.plot(x,y, label = 'Sample Label')
plt.title('Sample plot Title')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.grid(True)

#add footnote
plt.figtext(1970,2020,'Footnote',ha='right',va='bottom')

#add legend, location pick the best automatically
plt.legend(loc='best', framealpha=0.5, prop={'size':'small'})

