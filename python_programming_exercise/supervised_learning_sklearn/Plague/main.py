 #Time Series Estimation of plague
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from math import sqrt

# dateparse = lambda dates:pd.datetime.strptime(dates, '%d/%m/%Y %I:%M:%S %p')
# names=['DateTime','TempOut','HiTemp','LowTemp','OutHum','DewPt','WindSpeed','WindRun','WindChill','HeatIndex','THWIndex','Bar','Rain','RainRate','HeatDD','CoolDD','InTemp','InHum','InDew','InHeat','InEMC','InAirDensity','WindSamp','WindTx','ISSRecpt','ArcInt']
df_input=pd.read_csv('D:\\Python_programs\\datasets\\plague-dataset\\train.csv',low_memory=False)#parse_dates=['DateTime'],index_col='DateTime')
df_input['date_parsed'] = pd.to_datetime(df_input['DateTime'], infer_datetime_format=True)

# classes=['PA','PB','PC','PD','PE','PF','PG']
# df_classes=pd.read_csv('D:\\Python_programs\\datasets\\plague-dataset\\train.csv',names=classes)

# print(df_input.columns)
# print(df_classes.columns)
# print(type(df['DateTime'][0]))
print(df_input.describe())

# df_input.hist()
# plt.show()

# print(df.index)
# corrmat=df.corr()
# fig=plt.figure(figsize=(12,9))
# sns.heatmap(corrmat,vmax=1,square=True)
# plt.show()
#WindTx and Arcint doesnot have relation

# # Draw Plot
# def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
#     plt.figure(figsize=(16,5), dpi=dpi)
#     plt.plot(x, y, color='tab:red')
#     plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
#     plt.show()

# fig,(ax1,ax2)= plt.subplots(nrows=2,ncols=1,sharex=True)

# ax1.plot(df_input['date_parsed'],df_input['PA'])
# ax2.plot(df_input['date_parsed'],df_input['PB'])

# plt.tight_layout()
# plt.show()


from statsmodels.tsa.stattools import adfuller, kpss
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])
# print('df_input_values:',df_input.values)
# # ADF Test
for classification in ['PA','PB','PC','PD','PE','PF','PG']:
    result = adfuller(df_input[classification], autolag='AIC')
    print(f'ADF Statistic {classification}: {result[0]}')
    print(f'p-value: {result[1]}')
    for key, value in result[4].items():
        print('Critial Values:')
        print(f'  {key}, {value}')

# # KPSS Test
for classification in ['PA','PB','PC','PD','PE','PF','PG']:
    result = kpss(df_input[classification], regression='c')
    print('\nKPSS Statistic:',classification,' %f' % result[0])
    print('p-value: %f' % result[1])
    for key, value in result[3].items():
        print('Critial Values:')
        print(f'   {key}, {value}')

#Estimating and eliminating trend
for classification in ['PA','PB','PC','PD','PE','PF','PG']:
    ts_log=np.log(df_input[classification])
    print('datatype of ts_log:',type(ts_log))
    print('ts_log: ',ts_log)
    plt.plot(ts_log)
    plt.show(block=False)

# print(df.head())
# print(df.values)

# plot_df(df, x=df['date_parsed'], y=df['date_parsed'], title='Number of patients who will be affected by the Plague Pathogens A- G from July 2040 till April 2040.')

# # Fit the model to the training data
# # my_model.fit(X, y)

# # # Generate test predictions
# # preds_test = my_model.predict(X_test)

# # from sklearn.metrics import accuracy_score,mean_squared_error
# # # test_preds = model.predict_classes(test)
# # # accuracy_score(test_target, test_preds)
# # meanSquaredError=mean_squared_error(test_target,test_pred)
# # rootmeanSquaredError=sqrt(meanSquaredError)

# # # Save predictions in format used for competition scoring
# # output = pd.DataFrame({'ID': X_test.index,
# #                        'PA': preds_test,
# #                        'PB':preds_test,
# #                        'PC':preds_test,
# #                        'PD':preds_test,
# #                        'PE':preds_test,
# #                        'PF':preds_test,
# #                        'PG':preds_test})
# # output.to_csv('submission.csv', index=False)