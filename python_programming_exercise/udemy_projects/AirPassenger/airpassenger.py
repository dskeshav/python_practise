import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('AirPassengers.csv')
print( data.head())
print( '\n Data Types:')
print( data.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
print( data.head())

print(data.index)
print("datashape: ",data.shape)

ts = data['#Passengers'] 
print(ts.head(10))

#Indexing technique for TS data
#1. Specify the index as a string constant
print('ts index as a string constant: ',ts["1949-01-01"])

#2. Import the datetime library and use 'datetime' function:
from datetime import datetime
print("ts index as a datetime constant: ",ts[datetime(1949,1,1)])

print('entire range:\n',ts['1949-01-01':'1949-05-01'])

print('indices ends: ',ts[:'1949-05-01'])

print('1949:\n',ts['1949'])

plt.plot(ts)
print("print")

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
#Determing rolling statistics
    rolmean=pd.rolling_mean(timeseries,window=12)