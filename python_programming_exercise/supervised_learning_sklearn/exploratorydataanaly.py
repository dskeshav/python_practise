from sklearn import datasets
import numpy
import scipy
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

iris=datasets.load_iris()

X=iris.data
y=iris.target
df=pd.DataFrame(X,columns=iris.feature_names)

print(df.head())

pd.plotting.scatter_matrix(df,c=y,figsize=[8,8],s=150,marker="D")
