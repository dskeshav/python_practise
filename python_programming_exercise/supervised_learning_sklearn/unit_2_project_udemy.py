#Supervised Learning Project
import pandas
import numpy
#plotting module
import matplotlib.pyplot as plotting
from pandas.plotting import scatter_matrix
#model building
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
#Reporte module
from sklearn.metrics import classification_report ,confusion_matrix , accuracy_score


#Load the Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print(dataset.feature_names)

#Dataset Properties
# #shape
# print(dataset.shape)
# #head
# print(dataset.head(20))
# #describe
# print(dataset.describe())

# # #class distribution
# print(dataset.groupby('class').size())

# #Data Visualization
dataset.hist()
plotting.show()

# #scattered plot matrix
scatter_matrix(dataset)
plotting.show()


#Evaluate Algorithms

#Create Validation dataset
array=dataset.values
X=array[:,0:4]
y=array[:,4]
validation_size=0.20
seed=7
X_train,X_validation,y_train,y_validation=model_selection.train_test_split(X,y,test_size=validation_size,random_state=seed)

#10 -fold Cross Validation dataset
seed=7
scoring='accuracy'

#build model

models=[]
models.append(('LR',LogisticRegression()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('SVM',SVC()))

results=[]
names=[]

for name,model in models:
    kfold=model_selection.KFold(n_splits=10,random_state=seed)
    cv_results=model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)"%(name,cv_results.mean(),cv_results.std())
    print(msg)
    

for name, model in models:
    model.fit(X_train, y_train)
    print("X_Validation",X_validation)
    predictions = model.predict(X_validation)
    print(name)
    print(accuracy_score(y_validation, predictions))
    print(classification_report(y_validation, predictions))