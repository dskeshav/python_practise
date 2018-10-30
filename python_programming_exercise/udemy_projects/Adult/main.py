import csv 
import requests
from pandas.plotting import scatter_matrix
from sklearn import model_selection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

#get training dataset 
data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
names=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex',
        'capital-gain','capital-loss','hours-per-week','native-country','class']

dataset_data = pd.read_csv(data_url, names=names)
print(type(dataset_data))
print("dataset_data shape: ",dataset_data.shape)

#Raplace missing values ? with NaN
dataset_data[names]=dataset_data[names].replace(' ?',np.nan)

#Drop rows which contains NaN
dataset_data=dataset_data.dropna()
print("dataset_data shape after row removal:\n",dataset_data.shape)
print("dataset_data description:\n",dataset_data.describe())
print("dataset_data class:\n",dataset_data.groupby('class').size())

# Get test dataset
test_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"
dataset_test=pd.read_csv(test_url,names=names)
print("dataset_test shape: ",dataset_test.shape)
#drop the first index of test dataset due to invalid data  
dataset_test.drop(dataset_test.index[0], inplace=True)
# print("dataset_test shape: ",dataset_test.shape)


#Raplace missing values ? with NaN
dataset_test[names]=dataset_test[names].replace(' ?',np.nan)
dataset_test=dataset_test.dropna()
print('dataset_test shape after removal: ',dataset_test.shape)

#strip the period from the class column to maintain consistency with the training dataset 
dataset_test['class']=dataset_test['class'].str.strip('.')
print("dataset_test class:\n",dataset_test.groupby('class').size())
#target variable
target="class"

#Get all the columns from the dataframe
columns= dataset_data.columns.tolist()

#filter the columns to remove data we do not want
columns=[c for c in columns if c not in ['class','native-country','sex','race','relationship','education','occupation','marital-status','workclass']]
# print("columns :",columns)


#classifier algorithm
from sklearn import tree 
# from sklearntree import DecisionTreeClassifier  
from sklearn.naive_bayes import BernoulliNB,GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report ,confusion_matrix , accuracy_score

#time interval
import datetime

#models
models=[]
models.append(('CART_gini',tree.DecisionTreeClassifier(criterion='gini',min_samples_split=250,min_samples_leaf=20)))
models.append(('NB',GaussianNB()))
models.append(('BNB',BernoulliNB()))
models.append(('KNN1',KNeighborsClassifier(n_neighbors=1)))
models.append(('KNN3',KNeighborsClassifier(n_neighbors=3)))

results=[]
names=[]
training_time=[]

#10 -fold Cross Validation dataset
seed=7
scoring='accuracy'
for name,model in models:
    kfold=model_selection.KFold(n_splits=10,random_state=seed)
    cv_results=model_selection.cross_val_score(model, dataset_data[columns], dataset_data['class'], cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)"%(name,cv_results.mean(),cv_results.std())
    print(msg)

# print("results ",results,"\n",type(results))
for name, model in models:
    t1=datetime.datetime.now()
    model.fit(dataset_data[columns], dataset_data['class'])
    t2=datetime.datetime.now()
    predictions = model.predict(dataset_test[columns])

    print("type of predictions: ",type(predictions))
    print(name)
    print(accuracy_score(dataset_test['class'], predictions))
    print(classification_report(dataset_test['class'], predictions))
    training_time.append(np.array([round((t2-t1).total_seconds(),3)]))
    print("trining time of {}: ".format(model),round((t2-t1).total_seconds(),3))



# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



# # boxplot trianing time
# fig = plt.figure()
# fig.suptitle('Training time Comparison')
# ax = fig.add_subplot(111)
# plt.boxplot(training_time)
# plt.boxplot(results)
# ax.set_xticklabels(names)
# plt.show()
# #histogram representation of dataset
# # dataset_data.hist()
# # plt.show()

# # #Corelation matrix
# # corrmat=dataset_data.corr()
# # fig=plt.figure(figsize=(12,9))
# # sns.heatmap(corrmat,vmax=1,square=True)
# # plt.show()

# # # response=requests.get(data_url)
# # # with open("adult.data.csv",'w') as datacsv:
# # #     if response.status_code != 200:
# # #         print('Failed to get data:', response.status_code)
# # #     else:
# # #         wrapper = csv.reader(response.text.strip().split('\n'))
# # #     for record in wrapper:
# # #         csv



# #Corelation matrix
# # corrmat=dataset_test.corr()
# # fig=plt.figure(figsize=(12,9))
# # sns.heatmap(corrmat,vmax=.8,square=True)
# # plt.show()



# # data_url="https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
# # names=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex',
# #         'capital-gain','capital-loss','hours-per-week','native-country','class']
# # #write to adult.data file if empty
# # if (os.path.getsize("adult.data.csv")==0):
# #        with open("adult.data.csv",'w') as traindatafile:
# #                traindatafile.write(','.join(names))
# # else:
# #         print("empty file")
income_classify=tree.DecisionTreeClassifier(criterion='gini',min_samples_split=250,min_samples_leaf=20)
income_classify.fit(dataset_data[columns], dataset_data['class'])
# print(income_classify)
import graphviz

with open("income_classify.txt", "w") as f:
    f = tree.export_graphviz(income_classify, out_file=f,feature_names=dataset_data.features_name,  
                         class_names=dataset_data.target,  
                         filled=True, rounded=True)

# converting into the pdf file
with open("income_classify.pdf", "w") as f:
    f = tree.export_graphviz(income_classify, out_file=f)
