import csv 
import requests

import pandas as pd
import matplotlib.pyplot as plt

#write to adult.data file if empty

data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
names=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex',
        'capital-gain','capital-loss','hours-per-week','native-country']

dataset_data = pd.read_csv(data_url, names=names)
print(type(dataset_data))
print(dataset_data.shape)
# print(dataset_data["age"])

dataset_data=dataset_data.dropna(subset=[])
print(dataset_data.shape)

# dataset_data=dataset_data.dropna(dataset_data["age"]==" ?")
# print(dataset_data.shape)

# plt.hist(dataset_data["age"])
# plt.show()
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

