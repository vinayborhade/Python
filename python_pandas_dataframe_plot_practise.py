# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:04:07 2020

@author: Vinay Borhade
"""
import pandas as pd

path = "D:/OneDrive/MachineLearning/VB course/Repository/Python/Basics/"

# import a csv file
scrip = pd.read_csv(path + "idea_90.csv")

scrip.shape
scrip.columns

# Data transformation and filtering or subsetting

# using functions
def change_col_names(x):
    x = x.strip()
    x = x.replace(" ","_")
    x = x.upper()
    return(x)
scrip.rename(columns=change_col_names, inplace=True)

# using inline functions
scrip.rename(columns=lambda x: x.strip().replace(" ","_").lower(), inplace=True)

# convert date column to datetime while creating index  
scrip.index = pd.to_datetime(scrip.date)

#scrip.rename(index=pd.to_datetime(scrip.date), inplace=True)

# to change type of column
#scrip.date = pd.to_datetime(scrip.date)
#scrip.index = scrip.date
# date is used as index, remove dupliacte column
scrip.pop('date')

# filtering - get all rows less than 30 Apr 2018

# filtering using index
df = scrip.loc[scrip.index <= '2018-04-30']

# filtering on any column
df[df.close_price >= 70.0]

# creating new column using existing columns - Feature Engineering
scrip['price_change'] = scrip['close_price'] - scrip['open_price']

import matplotlib.pyplot as plt
plt.plot(scrip['close_price'])

df_m = scrip['close_price'].rolling(window=5).mean()
plt.plot(df_m)

df_p = scrip['close_price'].pct_change()
plt.plot(df_p)

# between from and to
df = scrip.loc[(scrip.index > '2018-04-30') & (scrip.index <= '2018-05-10') & (scrip.close_price > 60) & (scrip.symbol == 'IDEA')]

df = scrip.loc[(scrip.index == '2018-04-30') | (scrip.index == '2018-05-31')]
df['price_change'] = df['close_price'] - df['open_price']


df = scrip.loc[(scrip.index == '2018-04-30') | (scrip.index == '2018-05-31'), ['series', 'symbol']]

scrip.loc[(scrip.index == '2018-04-30') | (scrip.index == '2018-05-31'), 'series'] = 'EQ_MTH_END'

scrip.loc[(scrip.index == '2018-04-30') | (scrip.index == '2018-05-31'), ['close_price','open_price']] = scrip.loc[(scrip.index == '2018-04-30') | (scrip.index == '2018-05-31'), ['close_price','open_price']] + 100 

###################################################################
          
# Example For Feature Engineering
    
data_1 = pd.read_excel(path + "interest_rates.xlsx")
data_1["inter_comp"] = data_1["Term"]* data_1["Loan Amount"] * data_1["Interset Rates"] / 100
data_1["Outstanding"] = data_1["inter_comp"] +  data_1["Loan Amount"]

data_1["Start Date"] = pd.to_datetime(data_1["Start Date"])

def get_end_date(s_dt, term):
    #print(s_dt, term)
    return(pd.date_range(s_dt, periods=term*12, freq='M')[-1])
data_1["End_Date"] = data_1.apply(lambda x: get_end_date(x['Start Date'], x['Term']), axis=1)

data_1["EMI"] = data_1["Outstanding"] / (data_1["Term"]* 12)

from datetime import date, timedelta

first_day_of_current_month = date.today().replace(day=1)
data_1["Last_Month_End"] = first_day_of_current_month - timedelta(days=1)

def get_pending_months(lst_mth_end, s_dt):
    #print(s_dt, term)
    return(pd.Timestamp(lst_mth_end).to_period("M") - pd.Timestamp(s_dt).to_period("M"))
    
data_1["Pending Months"] = data_1.apply(lambda x: get_pending_months(x['Last_Month_End'], x['Start Date']), axis=1)

data_1["Paid"] = ((data_1["Term"]* 12) - data_1["Pending Months"]) * data_1["EMI"]

data_1["Outstanding"] = data_1["Outstanding"] - data_1["Paid"]

data_1["Status"] = data_1["Pending Months"].apply(lambda x: "Completed" if x == 0 else "Ongoing")
#data_1['Total_amt'].sum()

#using function and df.apply() insstead of for loop
data_1.to_excel(path + "interest_rates_transformed.xlsx")


a = data_1["Start Date"]
b= data_1["Term"]
l = []
for i in range(len(a)):
        end = a[i] + pd.DateOffset(years=b[i]) 
        l.append(end)

data_1["End_date"] = l
    
# using a explicit for loop
a = data_1["Start Date"]
t = data_1["Term"]
m = list(zip(a, t))
l = []
for i in m:
    date = i[0]
    term = i[1]
    l.append(get_end_date(date, term)) 
    
data_1["End_data"] = l

# using a explicit for loop
   

#################################################################################
# derieving a cnew column using two columns with apply function 
#transformation usin gapplyt and lambda

import pandas as pd

df = pd.DataFrame({'ID':['1', '2', '3'], 'col_1': [0, 2, 3], 'col_2':[1, 4, 5]})

def get_1_params(sta):
    print(sta)
    
df['col_1'].apply(get_1_params)

df.apply(lambda x: get_1_params(x.col_1), axis=1)

def get_2_params(sta, end):
    print(sta , end)
    
df.apply(lambda x: get_2_params(x.col_1, x.col_2), axis=1)

#################################################################################

# Grouping on data

      # Aggregations (count, sum, mean, std)
      # Filters(on aggregate)

import pandas as pd
import numpy as np

#ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#   'Rank': [1, 2, 2, 3, 3, 4 ,1 ,1, 2 , 4, 1,2],
#   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
ipl_data = pd.read_excel(path + "ipl_data.xlsx")

ipl_data['Team'] = ipl_data['Team'].str.title()

ipl_data.groupby('Team')

ipl_data.groupby('Team').groups

ipl_data.groupby(['Team','Rank']).groups

grouped = ipl_data.groupby('Team')

for name, group in grouped:
   if group['Points'] > 800:
       print(group)

grouped.get_group('Devils')

avg = grouped['Points'].agg(np.mean)
plt.bar(avg.index, avg)

grouped = ipl_data.groupby('Team')
grouped.agg(np.size)

stats = grouped['Points'].agg([np.sum, np.mean, np.std])

plt.bar(stats.index, stats['sum'])

score = lambda x: (x - x.mean()) / x.std()*10
grouped.transform(score)

# how many teams have played more than two season
ipl_data.groupby('Team').filter(lambda x: len(x) > 2)

ipl_data.groupby('Team').filter(lambda x: x['Points'].mean() > 770)

data_2 = pd.read_excel("D:/OneDrive/imarticus/data/interest_rates_transformed.xlsx")

data_2.groupby('Name').groups
 
name_grp = data_2.groupby('Name')
name_grp['Loan Amount'].agg(np.sum)

bank_grp = data_2.groupby('Bank')
bank_grp['Loan Amount'].agg(np.sum)


bank_type_grp = data_2.groupby(['Bank','Type'])
bank_type_grp['Loan Amount'].agg(np.sum)

ipl_data[ipl_data['Points'] > 800]

############################################################################

# Plotting or graphs -- plot.py (matplotlib, seaborn)
   # both columns numerical - scatter plot, lmplot, stripplot, pairplot 
   # 1 numerical and 1 categorical  - factorplot, catplot
   # both categorical
          # first you have to group by and get count to plot
          # then use cat or factor plot

import seaborn as sns
import pandas as pd
import numpy as np
tips = sns.load_dataset('tips') 

a = tips.groupby(["day","time"])
a.sum()

grouped_data=tips.groupby('time')
grouped_data.sum()
grouped_data.count()

tips['tip_percent'] = (tips['tip'] / tips['total_bill'])*100

tips['bill_per_head'] = (tips['total_bill'] / tips['size'])

grouped_tips = tips.groupby('sex')
grouped_tips['tip'].mean()
grouped_tips['tip'].count()
grouped_tips['tip_percent'].mean()



titanic = sns.load_dataset('titanic') 


grouped_time = tips.groupby(["sex", "time", "day"])
grouped_time['tip_percent'].mean()
grouped_time['tip'].mean()

grouped_smoker = tips.groupby(["smoker"])
grouped_smoker['tip_percent'].mean()
grouped_smoker['tip'].mean()

grouped_smoker = tips.groupby(["smoker", "day", "time"])
grouped_smoker.count()
grouped_smoker['total_bill'].sum()
grouped_smoker['tip_percent'].mean()

grouped_day = tips.groupby(["day"])
grouped_day.count()
grouped_day['total_bill'].sum()

fri = grouped_day.filter(lambda x: x['total_bill'].sum() < 1000)
fri.groupby(["time"])['total_bill'].sum()

def my_plot(cat_col, grouping_col, data, y_col_type="count"):
    
    norm = None
    
    if y_col_type == "count":
        norm = False
        
    elif y_col_type == "percent":
        norm = True
        
    df1 = data.groupby(cat_col)[grouping_col].value_counts(norm)
    if y_col_type == "percent":
        df1 = df1.mul(100)
    df1 = df1.rename(y_col_type).reset_index()
    
    g = sns.catplot(x=cat_col,y=y_col_type,hue=grouping_col, kind='bar', data=df1)
    if y_col_type == "percent":
        g.ax.set_ylim(0,100)
    g.set_xticklabels(rotation=65, horizontalalignment='right')

my_plot('time', 'size', tips, "count")