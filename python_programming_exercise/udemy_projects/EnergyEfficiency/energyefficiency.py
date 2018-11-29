# UCI repository link
# https://archive.ics.uci.edu/ml/datasets/Energy+efficiency

# Reserach paper
# http://people.maths.ox.ac.uk/tsanas/Preprints/ENB2012.pdf
# https://www.dataquest.io/blog/excel-and-pandas/
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_excel('ENB2012_data.xlsx')

print(dataset.head())

# plt.hist(dataset)
# plt.show()

print(dataset.shape)

# #target variable
# target=['Y1','Y2']

# #Get all the columns from the dataframe
# columns= dataset.columns.tolist()


# columns=[c for c in columns if c not in target]

#Corelation matrix
corrmat=dataset.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=1.0,square=True,annot=True)
plt.show()
# colors=['red','green']
# plt.scatter(columns, target, c=colors)
# plt.show()




#classifier algorithm
from sklearn import tree ,model_selection
from  sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
# from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error

# # dtc=tree.DecisionTreeRegressor(criterion='mse',min_samples_split=2,min_samples_leaf=20)
# # # gnb=GaussianNB()
# # # bnb=BernoulliNB()
# # # knn1=KNeighborsClassifier(n_neighbors=1)
# # # knn3=KNeighborsClassifier(n_neighbors=3)
lr=LinearRegression()
svr=SVR()

#models
models=[]
models.append(('LR',lr))
models.append(('SVR',svr))
# # models.append(('CART_mse',dtc))
# # # models.append(('NB',gnb))
# # # models.append(('BNB',bnb))
# # # models.append(('KNN1',knn1))
# # # models.append(('KNN3',knn3))

results=[]
names=[]
training_time=[]
# #10 -fold Cross Validation dataset
seed=7


#target variable
target=['Y1','Y2']

#Get all the columns from the dataframe
columns= dataset.columns.tolist()


columns=[c for c in columns if c not in target]

for name,model in models:
    kfold=model_selection.KFold(n_splits=10,random_state=seed)
    cv_results=model_selection.cross_val_score(model, dataset[columns], dataset[target], cv=kfold, scoring='neg_mean_absolute_error')
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)"%(name,cv_results.mean(),cv_results.std())
    print(msg)


# # import datetime
# # # print("results ",results,"\n",type(results))
# # for name, model in models:
# #     t1=datetime.datetime.now()
# #     model.fit(dataset_data[columns], dataset_data['class'])
# #     t2=datetime.datetime.now()
# #     predictions = model.predict(dataset_test[columns])

# #     print("type of predictions: ",type(predictions))
# #     print(name)
# #     print(accuracy_score(dataset_test['class'], predictions))
# #     print(classification_report(dataset_test['class'], predictions))
# #     training_time.append(np.array([round((t2-t1).total_seconds(),3)]))
# #     print("trining time of {}: ".format(model),round((t2-t1).total_seconds(),3))

