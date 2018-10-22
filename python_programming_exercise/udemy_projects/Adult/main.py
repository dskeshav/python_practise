import csv 
import requests
from pandas.plotting import scatter_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#write to adult.data file if empty

data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
names=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex',
        'capital-gain','capital-loss','hours-per-week','native-country']

dataset_data = pd.read_csv(data_url, names=names)
print(type(dataset_data))
print(dataset_data.shape)
# print(dataset_data["age"])

target=["capital-gain","capital-loss"]


# dataset_data=dataset_data.dropna(dataset_data["capital-gain"]==0)
# print(dataset_data.shape)
# pd.plotting.scatter_matrix(dataset_data,c=names,figsize=[8,8],s=150,marker='D')

dataset_data.hist()
plt.show()
# plt.hist(dataset_data['capital-gain','capital-loss'])
# plt.show()

# scatter_matrix(dataset_data)
# plt.show()

#Corelation matrix
corrmat=dataset_data.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()
# response=requests.get(data_url)
# with open("adult.data.csv",'w') as datacsv:
#     if response.status_code != 200:
#         print('Failed to get data:', response.status_code)
#     else:
#         wrapper = csv.reader(response.text.strip().split('\n'))
#     for record in wrapper:
#         csv

#write to adult.test if empty
test_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"
dataset_test=pd.read_csv(test_url,names=names)
print(dataset_test.shape)


plt.hist(dataset_test['capital-gain'])
plt.show()

#Corelation matrix
corrmat=dataset_test.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()