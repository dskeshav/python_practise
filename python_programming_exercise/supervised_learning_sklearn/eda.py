from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

iris=datasets.load_iris()

X=iris.data
y=iris.target
print(datasets)
df=pd.DataFrame(X,columns=iris.feature_names)
pd.plotting.scatter_matrix(df,c=y,figsize=[8,8],s=150,marker='D')

plt.plot()
plt.show()

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X,y)


print(iris['data'].shape)
print(iris['target'].shape)

prediction=knn.predict(X_new)
print('Prediction {}'.format(prediction))



# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()

# plt.figure()
# df=df.cumsum()
# df.plot()

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot().


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

print(dataset.groupby('class').size())
dataset.hist()
plt.show()