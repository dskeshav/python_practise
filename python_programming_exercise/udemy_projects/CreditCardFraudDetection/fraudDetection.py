import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn


# Load the dataset from the csv file
data=pd.read_csv('creditcard.csv')

print(data.columns) 
# V1 to V28 these are result of PCA reduction in order to protect 
# the sensitive data

print (data.shape)

print(data.describe())


data =data.sample(frac=0.1,random_state=1)

print(data.shape)

#Plot histogram for each parameter
data.hist(figsize=(30,30))
plt.show()

#Determine number of fraude cases in dataset
Fraud =data[data['Class']==1]
Valid= data[data['Class']==0]

outlier_fraction=len(Fraud)/float(len(Valid))
print(outlier_fraction)

print("Fraud cases: {}".format(len(Fraud)))
print("Valid cases: {}".format(len(Valid)))

#Correlation matrix
corrmat=data.corr()
fig=plt.figure(figsize=(12,9))

sns.heatmap(corrmat,vmax=0.8,square=True)
plt.show()

#Get all the colums in the dataframe
columns=data.columns.tolist()

#
columns=[c for c in columns if c not in ['Class']]

target="Class"

X=data[columns]
Y=data[target]

print(X.shape)
print(Y.shape)

from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.svm import SVC
 #return anamoly score of each sample
from sklearn.neighbors import LocalOutlierFactor 
#Is an Unsupervised outlier detection algorithm

#define a random state
state =1

#define the outlier
classifiers={
    "Isoloation Forest": IsolationForest(max_samples=len(X),
                                        contamination=outlier_fraction,
                                        random_state=state),
    "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20,
                                                contamination=outlier_fraction),
    "Support Vector Machine": SVC()
}

#FIt the model
n_outlier=len(Fraud)

for i,(clf_name,clf) in enumerate(classifiers.items()):

    #fit the data and tag putliers
    if clf_name=="Local Outlier Factor":
        y_pred=clf.fit_predict(X)
        scores_pred=clf.negative_outlier_factor_
    elif clf_name=="Isoloation Forest":
        clf.fit(X)
        scores_pred=clf.decision_function(X)
        y_pred=clf.predict(X)
    
    else:
        clf.fit(X,Y)
        scores_pred=clf.decision_function(X)
        y_pred=clf.predit()

    # Reshape the prediction values to 0 for valid,1 for invalid
    y_pred[y_pred==1]=0
    y_pred[y_pred==-1]=1

    n_errors=(y_pred !=Y).sum()

    print('{}: {}'.format(clf_name,n_errors))
    print(accuracy_score(Y,y_pred))
    print(classification_report(Y,y_pred))


