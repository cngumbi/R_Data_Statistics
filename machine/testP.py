#dealing with data structures (series and dataframes) with pandas
#also import numpy to help in sorting the data
#uncommet the print statements to see th output
import pandas as ps
import numpy as ny
#import testN

#create a series by passing a list of values, and custom index label.

n = ps.Series([1,2,3,ny.nan,5,6], index=['A','B','C','D','E','F'])

#print(n)

#create a pandas dataframe

data = {'Gender':['F','M','M'],
        'Emp_ID':['E05','E06','E09'],
        'Age':[25,27,25]}

#so lets specify in columns parameter

#df = ps.DataFrame(data, columns = ['Emp_ID','Gender','Age'])

#print(df)

#reading data frome a csv file

"""df = ps.read_csv('Data/mtcars.csv') #from csv
df = ps.read_csv('Data/mtcars.txt', sep='\t') #from text file
df = ps.read_excel('Data/mtcars.xlsx','Sheet1') #from excel"""""

#reading from multiple sheets of same excel in =to different dataframes

"""xlsx = ps.ExcelFile('file_name.xls')
sheat1_df = ps.read_excel(xlsx, 'Sheet1')
sheet2_df = ps.read_excel(xlsx,'Sheet2')"""

#writing to file

#index = False will not write the index values, default is True

"""df.to_csv('Data/mtcars_new.csv', index = False)
df.to_csv('Data/mtcars_new.txt', sep='\t', index = False)
df.to_excel('Data/mtcars.new.xlsx', sheet_name = 'Sheet1', index = False)"""

#basic Statistics on DataFrame
#describe() will return the stats such as count, mean, standard deviation, min
#1st quartile, median, 3rd quartile, and max

#df = ps.read_csv('Data/iris.csv')

#df.describe()

#use covariance cov()
#it has a positive covariance meaning variables are positively related
#while negative covariance means the variables are inversely related
#its drawback is that it does not tell you the degree of positive or negative
# relation

#df.cov()

#use correlation to determine how two values are related
#corr()
#it also tell you the degree to which the variables tend to move together

#df.corr()

data = {
        'emp_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],
        'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']}

df_1 = ps.DataFrame(data, columns = ['emp_id','first_name','last_name'])

data = {
        'emp_id': ['4', '5', '6', '7'],
        'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],
        'last_name': ['Alexander', 'Suma', 'Mike', 'G']}

df_2 = ps.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])

#use concat to concatinate the data

#df = ps.concat([df_1,df_2])
#print(df)

#use append to do the same thing

#print(df_1.append(df_2))

#concatinate along a column

#print(ps.concat([df_1,df_2],axis = 1))

#merging or dataframes

#merge dataframe based on the id values
#only the id present oin both tables will be joined

#print(ps.merge(df_1, df_2, on='emp_id'))

#lets join the dataframes
#left join

#print(ps.merge(df_1, df_2, on='emp_id', how = 'left'))

#merge while adding a suffix to duplicate column names of both table

#print(ps.merge(df_1,df_2, on='emp_id', how='left', suffixes=('_left','_right')))

#right join two data frames

#print(ps.merge(df_1,df_2, on='emp_id', how = 'right'))

#use inner join

#print(ps.merge(df_1, df_2, on='emp_id', how='inner'))

df = ps.DataFrame({'Name' : ['jack', 'jane', 'jack', 'jane', 'jack', 'jane',
                             'jack', 'jane'],
                   'State' : ['SFO', 'SFO', 'NYK', 'CA', 'NYK', 'NYK', 'SFO', 'CA'],
                   'Grade':['A','A','B','A','C','B','C','A'],
                   'Age' : ny.random.uniform(24, 50, size=8),
                   'Salary' : ny.random.uniform(3000, 5000, size=8),})
    
#for odering use this code

"""d = ps.DataFrame(df, columns = ['Name', 'State', 'Age', 'Salary'])
print(d)"""

#find max age and sakary by name/state

#print(df.groupby(['Name','State']).max())

#create a pivot table

print(ps.pivot_table(df, values = 'Age', index = ['State', 'Name'],columns = ['Grade']))
