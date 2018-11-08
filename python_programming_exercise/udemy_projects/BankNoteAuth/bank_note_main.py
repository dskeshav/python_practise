from pandas.plotting import scatter_matrix
from sklearn import model_selection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plotting

import pickle

dataset=pd.read_csv('data_banknote.csv')

print(dataset.shape)



# scatter_matrix(dataset,color=colors)
# plotting.show()

# define colors list, to be used to plot survived either red (=0) or green (=1)
colors=['red','green']

# make a scatter plot
scatter_matrix(dataset,figsize=[20,20],marker='.',c=dataset.Class.apply(lambda x:colors[x]))
plotting.show()

#Corelation matrix
corrmat=dataset.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()

#Create Validation dataset
array=dataset.values
X=array[:,0:4]
y=array[:,4]
validation_size=0.20
seed=7
X_train,X_validation,y_train,y_validation=model_selection.train_test_split(X,y,test_size=validation_size,random_state=seed)
print("X_train size:",X_train.shape)
print("X_validation size:",X_validation.shape)
print("y_train size:",y_train.shape)
print("y_validation size:",y_validation.shape)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report ,confusion_matrix , accuracy_score
#10 -fold Cross Validation dataset
seed=7
scoring='accuracy'
models=[]
models.append(('kNN',KNeighborsClassifier(n_neighbors=5)))
models.append(('SVC',SVC()))
results=[]
names=[]
for name,model in models:
    kfold=model_selection.KFold(n_splits=10,random_state=seed)
    cv_results=model_selection.cross_val_score(model,X_train, y_train,cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)"%(name,cv_results.mean(),cv_results.std())
    print(msg)

# for name, model in models:
#     model.fit(X_train, y_train)
#     print("X_Validation",X_validation)
#     predictions = model.predict(X_validation)
#     print(name)
#     print(accuracy_score(y_validation, predictions))
#     print(classification_report(y_validation, predictions))


picModel=model.fit(X_train, y_train)


filename='bank_note.pkl'
pickle.dump(picModel,open(filename,'wb'))