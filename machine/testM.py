#plotting the graphs using matplotlib

import matplotlib.pyplot as plt
import pandas as ps
import numpy as ny

#create a simple bar and scatter plot

"""x = ny.arange(5)
y = (20,35,30,35,27)

plt.bar(x,y)

#print(plt.bar(x,y))

#if you need to close the figure use
#show() or close()
#eg plt.show() or plt.close()

#to plot a scatter plot

plt.scatter(x,y)
plt.show()

#create plot on DataFrame

df = ps.read_csv('Data/iris.csv')

#plot a histogram

df.hist() #plot a histogram
df.plot() #plot a line graph
df.boxplot() #plot a box plot"""

#you can customize your labels 

"""x = ny.linspace(0,20,1000) #evenly space values
y =ny.sin(x)

#customize axis labels
plt.plot(x,y, label = 'Sample Label')
plt.title('Simple plot title')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.grid(True)

#add footnote
plt.figtext(0.995,0.01, 'Footnate', ha='right',va='bootom')
plt.legend(loc = 'best', framealpha = 0.5,prop = {'size':'small'})

#tight_layout() can take keyword argument of pad, w_pad and h_pad
#these control the extra padding around the figure border and between suplots
#the pads are specified in fraction of fontsize
plt.tight_layout(pad=1)

#Saving chart to a file
plt.savefig('filename.png')

plt.close() #close the current window to allow new plot creation on 

print(plt.show())

#object oriantation customization

fig,ax = plt.subplots()
fig,(ax1,ax2,ax3) = plt.subplot(nrows=3,ncols=1,sharex=True,figsize=(8,4))
#iterate the axes within a figure
for ax in fig.get)_axes():
    pass # do something
"""
#using ax.plot()

x = ny.linspace(0,20,1000)
y = ny.sin(x)

fig = plt.figure(figsize=(8,4))

ax = fig.add_subplot(1,1,1)
ax.plot(x,y,'b-', linewidth=2, label = 'Sample label')

#add title, labels and legend
ax.set_ylabel('y axis label', fontsize = 16)
ax.set_xlabel('x axis label', fontsize = 16)
ax.legend(loc = 'best')
ax.grid(True)
fig.subtitle('Sample plot Title')
fig.tight_layout(pad = 1)
fig.savefig('filename.png', dpi = 125)