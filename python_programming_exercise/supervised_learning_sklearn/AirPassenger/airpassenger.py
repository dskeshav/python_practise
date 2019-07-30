import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# data = pd.read_csv('AirPassengers.csv')
# print( data.head())
# print("datashape: ",data.shape)
# print( '\n Data Types:')
# print( data.dtypes) # here datatype is object not the TS object.

#  In order to read the data as a time series 
# a special argument has to be passed to the read_csv method.
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
print(data.head())

#print the index of the data
print(data.index)
print("datashape: ",data.shape)

# print (data[:'1950-07']['#Passengers'] )
ts = data[:'1960-10']['#Passengers'] 
print(ts.head(10))

# Indexing technique for TS data
# 1. Specify the index as a string constant
# print('ts index as a string constant: ',ts["1949-01-01"])

#2. Import the datetime library and use 'datetime' function:
from datetime import datetime
# print("ts index as a datetime constant: ",ts[datetime(1949,1,1)])

#Entire range index
# print('Entire range:\n',ts[datetime(1949,1,1):datetime(1949,5,1)])
#End Index
# print('Indices ends: ',ts[:datetime(1949,5,1)])

# print('1949:\n',ts['1949'])

# print('Hist :')
# plt.hist(ts[:'1960-12-01'])
# plt.show(block=True)

# print('PLOT ')
# plt.plot(ts[:'1960-12-01'])
# plt.show()

#Function which tests the stationarity of the timeseries are:
# 1.rolling statistics 
# 2.Augmented Dickey Fuller
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

    #perform Augmented Dickey-Fuller test:
    print('Result of Dickey-Fuller Test:')
    dftest=adfuller(timeseries,autolag='AIC')
    print("dftest datatype:",type(dftest))
    print("dftest :",dftest)
    dfoutput=pd.Series(dftest[0:4],index=['Test Statistics','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key]=value
    print(dfoutput)

#Test Stationarity for time series dataset
test_stationarity(ts)

#from observation it is evident that timeseries 
#is not stationary(because Test Statistics> Critical Value)
#TS is non-stationary due 2 major reason
#1.Trend,2.Seasonality

#Estimating and eliminating trend
# ts_log=np.log(ts)
# print('datatype of ts_log:',type(ts_log))
# print('ts_log: ',ts_log)
# plt.plot(ts_log)
# plt.show(block=False)

# # So we can use some techniques to estimate or model this trend and 
# # then remove it from the series. Some of most commonly used are:
# # 1. Aggregation -average for monthly/average
# # 2. Smoothing- taking rolling avg
# # 3. Polynomial fitting -fit regression model

# #Moving Average(Smoothing) : 2 ways of doing this are: 
# # 1.Rolling,2.Exponential weighted average
# moving_avg=ts_log.rolling(window=12).mean()
# print('datatype of moving_avg:',type(moving_avg))
# plt.title('Moving_average')
# plt.plot(ts_log,label='log plot')
# plt.plot(moving_avg,color='red',label='moving')
# plt.show(block=False)

# ts_log_moving_avg_diff=ts_log-moving_avg
# print(ts_log_moving_avg_diff.head(12))

# #drop NaN values in the TS 
# ts_log_moving_avg_diff.dropna(inplace=True)
# test_stationarity(ts_log_moving_avg_diff)

# #Exponential weighted average of the series 
# expwighted_avg = ts_log.ewm(halflife=12).mean()
# print('datatype of expwighted_avg:\n',expwighted_avg)
# plt.title('EWM')
# plt.plot(ts_log)
# plt.plot(expwighted_avg, color='red')
# plt.show(block=False)

# ts_log_ewma_diff = ts_log - expwighted_avg
# ts_log_ewma_diff.dropna(inplace=True)
# test_stationarity(ts_log_ewma_diff)


# # The simple trend reduction techniques discussed before don’t work in all cases, 
# # particularly the ones with high seasonality. Lets discuss two ways of removing trend and seasonality:
# # 1. Differencing – taking the differece with a particular time lag
# # 2. Decomposition – modeling both trend and seasonality and removing them from the model.

# # 1. Differencing
# ts_log_diff = ts_log - ts_log.shift()
# plt.plot(ts_log_diff)

# ts_log_diff.dropna(inplace=True)
# test_stationarity(ts_log_diff)

# # 2. Decomposition
# from statsmodels.tsa.seasonal import seasonal_decompose
# decomposition = seasonal_decompose(ts_log)


# trend = decomposition.trend
# seasonal = decomposition.seasonal
# residual = decomposition.resid

# plt.subplot(411)
# plt.plot(ts_log, label='Original')
# plt.legend(loc='best')
# plt.subplot(412)
# plt.plot(trend, label='Trend')
# plt.legend(loc='best')
# plt.subplot(413)
# plt.plot(seasonal,label='Seasonality')
# plt.legend(loc='best')
# plt.subplot(414)
# plt.plot(residual, label='Residuals')
# plt.legend(loc='best')
# plt.tight_layout()
# plt.show()

# ts_log_decompose = residual
# ts_log_decompose.dropna(inplace=True)
# test_stationarity(ts_log_decompose)


# #ACF and PACF plots:
# from statsmodels.tsa.stattools import acf, pacf

# lag_acf = acf(ts_log_diff, nlags=20)
# lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')

# #Plot ACF: 
# plt.subplot(121) 
# plt.plot(lag_acf)
# plt.axhline(y=0,linestyle='--',color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.title('Autocorrelation Function')


# #Plot PACF:
# plt.subplot(122)
# plt.plot(lag_pacf)
# plt.axhline(y=0,linestyle='--',color='gray')
# plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
# plt.title('Partial Autocorrelation Function')
# plt.tight_layout()
# plt.show()


# from statsmodels.tsa.arima_model import ARIMA

# #AR Model
# plt.subplot(3,1,1)
# model = ARIMA(ts_log, order=(2, 1, 0))  
# results_AR = model.fit(disp=-1)  
# plt.plot(ts_log_diff)
# plt.plot(results_AR.fittedvalues, color='red')
# plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-ts_log_diff)**2))

# # MA Model
# plt.subplot(3,1,2)
# model = ARIMA(ts_log, order=(0, 1, 2))  
# results_MA = model.fit(disp=-1)  
# plt.plot(ts_log_diff)
# plt.plot(results_MA.fittedvalues, color='red')
# plt.title('RSS: %.4f'% sum((results_MA.fittedvalues-ts_log_diff)**2))


# import pickle
# # Combined Model
# plt.subplot(3,1,3)
# model = ARIMA(ts_log, order=(2, 1, 2))  
# results_ARIMA = model.fit(disp=-1)
# # creating pickle file  
# filename='airpassenger.pkl'
# pickle.dump(results_ARIMA,open(filename,'wb'))
# # np.save('model_bias.npy', [bias])
# plt.plot(ts_log_diff)
# plt.plot(results_ARIMA.fittedvalues, color='red')
# plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-ts_log_diff)**2))
# plt.tight_layout()
# plt.show()

# predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
# print( predictions_ARIMA_diff.head())

# predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
# predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff.cumsum(),fill_value=0)
# predictions_ARIMA_log.head()

# predictions_ARIMA = np.exp(predictions_ARIMA_log)
# plt.plot(ts)
# plt.plot(predictions_ARIMA)
# plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-ts)**2)/len(ts)))
# plt.show()