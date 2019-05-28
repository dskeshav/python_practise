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
# print(dataset.shape)
# print(dataset.head())

target=['y1','y2']
columns=[c for c in dataset.columns.tolist() if c not in target]
# Probability density estimates using histogram
# pointer=1
# fig1 = plt.figure()
# fig1.subplots_adjust(hspace=0.6, wspace=0.4)
# fig1.suptitle("Probability density estimates of input variables using histograms ", fontsize=14)
# for i in columns:
#         ax = fig1.add_subplot(4, 2, pointer)
#         pointer+=1
        
#         plt.ylabel('frequency')
#         plt.xlabel(i)
#         # print(dataset[i])
#         dataset[i].hist()
# plt.show()       


# fig2 = plt.figure()
# fig2.subplots_adjust(hspace=0.6, wspace=0.4)
# fig2.suptitle('Probability density estimates of output variables using histograms' , fontsize=14)
# pointer=1
# for i in target:
#         ax = fig2.add_subplot(2, 1, pointer)
#         pointer+=1
#         plt.ylabel('frequency')
#         plt.xlabel(i)
#         # print(dataset[i])
#         dataset[i].hist()
# plt.show()  

# Scattered plot for output y1,y2
# for i in target:
#     counter=1
#     fig=plt.figure()
#     fig.subplots_adjust(hspace=0.6, wspace=0.4)
#     fig.suptitle('Scattered plot wrt {}'.format(i),fontsize=14)
#     for j in columns:
#         ax = fig.add_subplot(4, 2, counter)
#         plt.xlabel(j)
#         plt.ylabel(i)
#         counter+=1
#         plt.scatter(dataset[j],dataset[i])
#     plt.show()

#Corelation matrix
corrmat=dataset.corr(method='spearman')
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=1.0,square=True,annot=True)
plt.show()

#Regression algorithm
from sklearn import tree ,model_selection
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mutual_info_score,mean_absolute_error

dtc=tree.DecisionTreeRegressor(criterion='mse',min_samples_split=2,min_samples_leaf=20)
lr=LinearRegression()
rfr=RandomForestRegressor()

# Spliting dataset into training and test  
# #Create Validation dataset
# array=dataset.values
# X=array[:,0:8]
# y=array[:,8:10]
# validation_size=0.20
# seed=7
# X_train,X_validation,y_train,y_validation=model_selection.train_test_split(X,y,test_size=validation_size,random_state=seed)
# print("X_train size:",X_train.shape)
# print("X_validation size:",X_validation.shape)
# print("y_train size:",y_train.shape)
# print("y_validation size:",y_validation.shape)

# #models
# models=[]
# models.append(('LR',lr))
# models.append(('RF',rfr))
# models.append(('CART_mse',dtc))

# results=[]
# names=[]
# training_time=[]
# # #10 -fold Cross Validation dataset
# seed=7

# #To find p-values
# import statsmodels.api as sm
# from scipy import stats

# X2 = sm.add_constant(dataset[columns])
# est = sm.OLS(dataset[target], X2)
# est2 = est.fit()
# print(est2.summary())

# # for name,model in models:
# #     kfold=model_selection.KFold(n_splits=10,random_state=seed)
# #     cv_results=model_selection.cross_val_score(model, dataset[columns], dataset[target], cv=kfold, scoring='neg_mean_absolute_error')
# #     results.append(cv_results)
# #     names.append(name)
# #     msg="%s: %f (%f)"%(name,cv_results.mean(),cv_results.std())
# #     print(msg)

# # import datetime
# # # print("results ",results,"\n",type(results))
# # for name, model in models:
# #     t1=datetime.datetime.now()
# #     model.fit(X_train, y_train)
# #     t2=datetime.datetime.now()
# #     predictions = model.predict(X_validation)
# #     print(predictions.shape)
# #     print("type of predictions: ",type(predictions))
# #     print(name)
# #     print(mean_absolute_error(y_validation, predictions))
# #     # print(mutual_info_score(y_validation, predictions))
# #     training_time.append(np.array([round((t2-t1).total_seconds(),3)]))
# #     print("trining time of {}: ".format(model),round((t2-t1).total_seconds(),3))

