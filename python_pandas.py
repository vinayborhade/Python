# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:00:28 2019

@author: Vinay Borhade
"""

##################################################################
#SERIES

import pandas as pd
s = pd.Series()
print(s)

import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = np.array(['1000000','1100000','800000','900000'])
s = pd.Series(data, index=[("Maruti", "Dzire"),["Hyundai", "Verna"],("Volkswagon", "Polo"), ("Skoda", "Rapid")])
print(s)

print(s[("Maruti", "Dzire")])

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)
#retrieve the first element
print(s[0])
print(s[:3])
print(s['a'])
print(s[['a','c','d']])

s['f'] = 6

print(s['f'])
##################################################################
#DATAFRAME
df = pd.DataFrame()
print(df)

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

data = [['Alex',[10,11,12]],['Bob',{'sports': True}],['Clarke',13]]
df = pd.DataFrame(data, columns=['Name','Marks'],dtype=float)
print(df)



data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])

df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
#With two column indic  es with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

print(df['one'])

df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four'] = df['one'] + df['three']
print(df)

df.loc['b']
df.loc[['b','c']]
print(df.iloc[3])
print(df.iloc[1:3])


del df['one']
print(df)

df.pop('two') # removes columns
print(df)

df = df.drop('b') # removes rows
print(df)

import pandas as pd

d1 = {'one' : pd.Series([5, 4, 7], index=['a', 'b', 'c']),
   'two' : pd.Series([3, 7, 8, 2], index=['a', 'b', 'c', 'd'])}

df_1 = pd.DataFrame(d1)
print(df_1)

df.append(df_1)


##################### UTILITY #####################


df = pd.DataFrame(d1)
print(df)

df.describe()

df.ndim

df.shape

df.size

df.values

df.head(2)
df.tail(2)

df.sum(axis=0)
df.sum(axis=1)

df.mean(axis=0)
df.mean(axis=1)

df.cumsum(axis=0)

import numpy as np

def div(x):
    return(x/5)

df.apply(div, axis=0)

#meadian, count, mode, median, min, max, std, prod, cumsum

#########################################################
d = {'one' : pd.Series([2, 1, 4, 4], index=['a', 'b', 'c', 'd']),
   'two' : pd.Series([11, 2, 13, 4], index=['a', 'b', 'c', 'd'])}

for k,v in d.items():
    print(k, v)

df = pd.DataFrame(d)
print(df)

for col_name in df:
   print(col_name)

col = 'two'

for col_name in df:
   print(col_name)
   if col_name == col:
       print(df[col_name])
   
for key, value in df.iteritems():
    if key == 'one':
       value['c'] = 4

   
for row_index, row in df.iterrows():
   print(row_index)
   print(row)
   
for row in df.itertuples():
    print(row)
    
for index, row in df.iterrows():
    if index == 'a':
       print(row)
       row['one'] = 3

print(df)

sorted_df = df.sort_values(by='one')
print(sorted_df)

sorted_df = df.sort_values(by=['one', 'two'])
print(sorted_df)

sorted_df = df.sort_values(by=['one', 'two'], kind='mergesort')
print(sorted_df)

###############################################################

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s)

print(s.str.lower())
print(s.str.upper())
print(s.str.len())

#s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t',])
print(s.str.split())
print(s.str.split(' '))
print(s.str.split('@'))

#s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t',])
print(s.str.cat(sep='_'))
print(s.str.cat(sep=' '))
print(s.str.cat(sep=','))
print(s.str.cat(sep='|'))
print(s.str.cat(sep='~'))
print(s.str.cat(sep='^'))

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t',])
print(s.str.get_dummies())

print(s.str.contains('@'))

print(s.str.replace('@', '$'))
print(s.str.count('m'))
print(s.str.startswith('T'))
print(s.str.endswith('t'))
print(s.str.contains('e'))
print(s.str.find('e'))
print(s.str.findall('e'))
print(s.str.swapcase())
print(s.str.islower())
print(s.str.isupper())
print(s.str.isnumeric())

##################################################################
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

import matplotlib.pyplot as plt
plt.plot(s.pct_change())
plt.plot(s)

df = pd.DataFrame(np.random.randn(5, 2))
print(df)
print(df.pct_change())

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1)
print(s2)
print(s1.cov(s2))

print(s1.corr(s2))

df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(df['a'].cov(df['b']))
print(df.cov())

print(df)
print(df['a'].corr(df['b']))
print(df.corr())

s = pd.Series(np.random.randn(5), index=list('abcde'))
print(s)
print(s.rank())

df = pd.DataFrame(np.random.randn(15, 4),
   index = pd.date_range('1/1/2000', periods=15),
   columns = ['A', 'B', 'C', 'D'])
print(df)
print(df.rolling(window=3).mean())
##################################################################
df_m = df.rolling(window=3).mean()
df_m.notnull()
df_m.isnull().any()
df_m.isnull().sum()

df_m.fillna(0)
df_m.fillna(method='backfill')
df_m.dropna()

df_m = df_m.replace({np.nan: 0.0})
df_m.replace({0.519535: 1})
df_m['A'] = df_m['A'].replace({np.nan: 0.0})

#######################################################################
scrip = pd.read_csv("D:/OneDrive/imarticus/data/idea_90.csv")
scrip.rename(columns=lambda x: x.strip(), inplace=True)
scrip.shape
scrip.columns
scrip.rename(columns=lambda x: x.replace(" ","_"), inplace=True)