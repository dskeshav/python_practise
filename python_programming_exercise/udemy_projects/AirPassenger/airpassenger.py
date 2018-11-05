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
plt.hist(ts)
plt.show(block=Fa)
plt.plot(ts)
plt.show()
print("print")

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    #Determing rolling statistics
    rolmean=timeseries.rolling(window=12).mean()
    rolstd=timeseries.rolling(window=12).std()

    #plot rolling statistics:
    orgi=plt.plot(timeseries,color='blue',label='Original')
    mean=plt.plot(rolmean,color='red',label='Rolling Mean')
    std=plt.plot(rolstd,color='black',label='Rolling std')

    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    
    df = pd.DataFrame(index=ts.index, columns=[orgi,mean,std])
    df = df.cumsum()
    plt.figure()
    df.plot()
    plt.show()

    #perform Dickey-Fuller test:
    print('Result of Dickey-Fuller Test:')
    dftest=adfuller(timeseries,autolag='AIC')
    dfoutput=pd.Series(dftest[0:4],index=['Test Statistics','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key]=value
    print(dfoutput)

#Test Stationarity for time series dataset
test_stationarity(ts)


