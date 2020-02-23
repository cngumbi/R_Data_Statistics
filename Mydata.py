#import the tabulate to create python tables
from tabulate import tabulate
#new libraris
import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


#mydata = []
mydata = [("chris", "25","programmer"),
            ("john","46","enginier"),
            ("peter","78","doctor")]







#create the head of the data
#headers = ["PT","AU ","TI","SO","VL","BP","EP","AR","DI","PD","PY","ZB","ZR","Z8","TC","ZS","Z9","SN","UT"]
headers = ["name","year","occupation"]
#print the table created
#print(tabulate(mydata, headers = headers, tablefmt = "grid"))

bigData = tabulate(mydata, headers = headers, tablefmt = "grid")

#print(bigData)

df = pd.read_csv(bigData)

print(df)