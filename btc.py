import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Loading the Data and Sorting the dates
df=pd.read_csv('BTC-2017min.csv')
df['date']=pd.to_datetime(df['date'])
df=df[(df['date']>'2017-12-01')&(df['date']<='2017-12-31')]

# # Creating Line Charts 
plt.figure(figsize=(14,6))
plt.subplot(2,2,1)
sns.lineplot(x='date', y='high', data=df, color='orange', label='BTC High Price', linewidth=2)
plt.xlabel('Dates')
plt.ylabel('High')
plt.title('BTC PRICE FOR 30 DAYS',fontsize=13,fontweight='bold')
plt.grid(axis='y')
plt.legend()

# Creating Histogram
plt.subplot(2,2,2)
sns.histplot(df['low'],bins=30,kde=True,color='skyblue',edgecolor='black',label='BTC VOLUME')
plt.title('Distribution of Bitcoin Low Prices', fontsize=13, fontweight='bold')
plt.xlabel('Low Price of Bitcoin)')
plt.ylabel('Frequency')
plt.legend()

# Creating Bar Plots
plt.subplot(2,2,3)
sns.barplot(x='date',y='Volume BTC',data=df,edgecolor='black',color='skyblue')
plt.xlabel('Dates')
plt.ylabel('Volume of BTC-USD')
plt.legend()

# Creating ScatterPlot
plt.subplot(2,2,4)
sns.scatterplot(x='date',y='low',hue='symbol',data=df)
plt.legend()

plt.suptitle('BITCOIN PRICE Visualization OF 30 DAYS',color='darkblue',fontsize=18,fontweight='bold')

plt.tight_layout()




