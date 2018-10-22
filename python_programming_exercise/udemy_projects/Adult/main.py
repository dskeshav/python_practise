import csv 
import requests
from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#write to adult.data file if empty
data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
names=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex',
        'capital-gain','capital-loss','hours-per-week','native-country','class']

dataset_data = pd.read_csv(data_url, names=names)
# print(type(dataset_data))
print("dataset_data shape: ",dataset_data.shape)
print(dataset_data.describe())
print(dataset_data.groupby('class').size())

#write to adult.test if empty
test_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"
dataset_test=pd.read_csv(test_url,names=names)
print("dataset_test shape: ",dataset_test.shape)

#target variable
target="class"
#Get all the columns from the dataframe
columns= dataset_data.columns.tolist()


#filter the columns to remove data we do not want
columns=[c for c in columns if c not in ['class','native-country','sex','race','relationship','education','occupation','marital-status','workclass']]


#classifier algorithm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error

#10 -fold Cross Validation dataset
seed=7
scoring='accuracy'

#models
DTC=DecisionTreeClassifier()
BNB=BernoulliNB()
KNN=KNeighborsClassifier()

# Fit the model class
DTC.fit(dataset_data[columns],dataset_data['class'])

#Generate predictions for test set
predictions=DTC.predict(dataset_test[columns])

# Compute accuracy between our test predictions
msr=mean_squared_error(predictions,dataset_test[target])
print("mean square error: ",msr)

# dataset_data=dataset_data[dataset_data.names !=' ?']

# dataset_data[].replace(' ?',pd.np.NaN)
# print("after replace: ",dataset_data.shape)
# print(dataset_data[dataset_data==pd.np.NaN].iloc[0])
# dataset_data.dropna(inplace=True)
# print("After drop: ",dataset_data.shape)
# pd.plotting.scatter_matrix(dataset_data,c=names,figsize=[8,8],s=150,marker='D')



#histogram representation of dataset
# dataset_data.hist()
# plt.show()



# #Corelation matrix
# corrmat=dataset_data.corr()
# fig=plt.figure(figsize=(12,9))
# sns.heatmap(corrmat,vmax=1,square=True)
# plt.show()
# # response=requests.get(data_url)
# # with open("adult.data.csv",'w') as datacsv:
# #     if response.status_code != 200:
# #         print('Failed to get data:', response.status_code)
# #     else:
# #         wrapper = csv.reader(response.text.strip().split('\n'))
# #     for record in wrapper:
# #         csv


# # plt.hist(dataset_test['capital-gain'])
# # plt.show()

# # #Corelation matrix
# # corrmat=dataset_test.corr()
# # fig=plt.figure(figsize=(12,9))
# # sns.heatmap(corrmat,vmax=.8,square=True)
# # plt.show()