# Import the Matplotlib module
import matplotlib.pyplot as plt

# Use a list to store the daily temperature
t = [22.2,22.3,22.5,21.8,22.5,23.4,22.8]

# Plot the daily temperature t as a line plot
plt.plot(t)
#plt.show()

#**************************************************************
# Prepare the data series
date = [12,13,14,15,16,17,18]
Tokyo = [15.3,15.4,12.6,12.7,13.2,12.3,11.4]
Hawaii = [26.1,26.2,24.3,25.1,26.7,27.8,26.9]
Hong_Kong = [22.3,20.6,19.8,21.6,21.3,19.4,21.4]

# Plot the lines for each data series
plt.plot(date,Tokyo)
plt.plot(date,Hawaii)
plt.plot(date,Hong_Kong)

#plt.show()

#**************************************************************

import matplotlib.pyplot as plt

# Prepare the data series
d = [12,13,14,15,16,17,18]
t0 = [15.3,15.4,12.6,12.7,13.2,12.3,11.4]
t1 = [26.1,26.2,24.3,25.1,26.7,27.8,26.9]
t2 = [22.3,20.6,19.8,21.6,21.3,19.4,21.4]

# Plot the lines for each data series
plt.plot(d,t0,label='Tokyo')
plt.plot(d,t1,label='Hawaii')
plt.plot(d,t2,label='Hong Kong')

# Set the limit for each axis
plt.xlim(12,18)
plt.ylim(10,30)
# Adding axis label
plt.xlabel('Date',size=10)
plt.ylabel('Temperature (°C)',size=10)
# Adding a grid
#plt.grid(True,linewidth=0.5,color='#ccc',linestyle='-')
# Adding a title 
plt.title("Daily Temperature of 3 cities in the second week of December", size=14, fontweight='bold')
# Adding a legend
plt.legend(loc='upper right' )
# Show the plot
plt.show()


plt.scatter(t2,t1)
plt.show()

#**************************************************************
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for NumPy function to keep the results reproducible
np.random.seed(42)

# Generate a 2 by 100 NumPy Array of random decimals between 0 and 1
r = np.random.rand(2,100)

# Plot the x and y coordinates of the random dots on a scatter plot
plt.scatter(r[0],r[1])

# Show the plot
plt.show()

wt = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
mileage = [26, 24.5, 24, 24, 22, 18, 17, 15, 14, 10]
plt.scatter(wt, mileage)
plt.show()

#**************************************************************
import matplotlib.pyplot as plt

# seed the random number generator to keep results reproducible
np.random.seed(123) 

# Generate 10 random numbers around 2 as x-coordinates of the first data series
x0 = np.random.rand(10)+1.5

# Generate the y-coordinates another data series similarly
np.random.seed(321) 
y0 = np.random.rand(10)+2
np.random.seed(456)
x1 = np.random.rand(10)+2.5
np.random.seed(789)
y1 = np.random.rand(10)+2
plt.scatter(x0,y0)
plt.scatter(x1,y1)

plt.show()
#**************************************************************
import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]

plt.bar(range(len(data)), data)

for i, v in enumerate(data):
    plt.text(i - .15, v - (v/2), str(v), color='black', fontweight='bold')
plt.show()
#**************************************************************

import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]

plt.barh(range(len(data)), data)
for i, v in enumerate(data):
    plt.text(v - (v/2), i, str(v), color='red', fontweight='bold')
plt.show()
#**************************************************************
import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(60)

plt.hist(X, bins = 30)
plt.show()
#**************************************************************
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(1000, 4)
plt.title('Box Plot by Category')
plt.boxplot(data)
plt.show()
#**************************************************************
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
tips =sns.load_dataset('tips') 
#import pandas as pd
#df = pd.read_csv('C:/Users/nikhil/OneDrive/imarticus/data/India_rainfall_act_dep_1901_2016_1.csv')

sns.lmplot(x= "total_bill", y='tip', data=tips)
#plt.show()
#**************************************************************
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex',                 
        palette='Set1')
plt.show()
#**************************************************************
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
plt.show()
#**************************************************************
sns.stripplot(x="day", y="tip", data=tips, jitter=True)
#**************************************************************
sns.stripplot(x='day', y='tip', data=tips, size=4, hue='smoker', jitter=True)
plt.ylabel('tip ($)') 
plt.show()
#**************************************************************
sns.pairplot(tips)
plt.show()

sns.lmplot(x='total_bill', y='tip', data=tips)
#**************************************************************
sns.pairplot(tips, hue='sex')
plt.show()

sns.factorplot("smoker", "total_bill", hue="sex", data=tips, kind="box")
plt.show()

sns.catplot("smoker", "total_bill", hue="sex", data=tips, kind="box")
plt.show()

sns.factorplot("smoker", "total_bill", hue="sex", data=tips, kind="box")
plt.show()


sns.factorplot("day", "total_bill", hue="sex", data=tips, kind="violin")
plt.show()

grp_day = tips.groupby('time')
df = grp_day['size'].count()

def my_percent_plot(cat_col, grouping_col, data):

    df1 = data.groupby(cat_col)[grouping_col].value_counts(normalize=True)
    df1 = df1.mul(100)
    df1 = df1.rename('percent').reset_index()
    
    g = sns.catplot(x=cat_col,y='percent',hue=grouping_col, kind='bar', data=df1)
    g.ax.set_ylim(0,100)
    g.set_xticklabels(rotation=65, horizontalalignment='right')


def my_count_plot(cat_col, grouping_col, data):

    df1 = data.groupby(cat_col)[grouping_col].value_counts(normalize=False)
    #df1 = df1.mul(100)
    df1 = df1.rename('count').reset_index()
    print(df1)
    g = sns.catplot(x=cat_col,y='count',hue=grouping_col, kind='bar', data=df1)
    #g.ax.set_ylim(0,100)
    g.set_xticklabels(rotation=65, horizontalalignment='right')
    
my_percent_plot('time', 'size', tips)

my_count_plot('time', 'size', tips)


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
        
#**************************************************************

from ggplot import *
ggplot(aes(x='total_bill', y='tip'), data=tips) + geom_point()
#**************************************************************
ggplot(aes(x='total_bill'), data=tips) + geom_histogram() + ggtitle("Histogram of Total Bill") + labs("total_bill", "Freq")
#**************************************************************
ggplot(aes(x='total_bill'), data=tips) + geom_density() + ggtitle("Density of Total Bill") + labs("total_bill", "Freq")
#**************************************************************
ggplot(aes(x='tip'), data=tips) + geom_bar() + ggtitle("Bar Chart of tip") 
#**************************************************************