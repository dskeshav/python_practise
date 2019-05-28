import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt

from sklearn import datasets

#load dataset
iris=datasets.load_iris()
features= iris.data
target=iris.target

# generate a pandas
df= pd.DataFrame(features)
df.columns=iris.feature_names

print(target)
print(iris.target_names)

print(df.shape)
print(df.head(20))
print(df.describe())

from pandas.plotting import scatter_matrix

scatter_matrix(df)
plt.show()

#elbow method to determine optimal number of cluster
from sklearn.cluster import KMeans

#empty x and y data lists
X=[]
Y=[]

for i in range(1,31):
    kmeans=KMeans(n_clusters =i)
    kmeans.fit(df)

    X.append(i)

    awcss= kmeans.inertia_/df.shape[0]
    Y.append(awcss)

plt.plot(X,Y,"bo-")
plt.xlim((1,30))
plt.xlabel('Number of Clusters')
plt.ylabel('Average Within-Cluster Sum of Squares')
plt.title('K-Means Clustering Elbow Method')

plt.show()

from sklearn.decomposition import PCA
from sklearn import preprocessing

#perform PCA
pca=PCA(n_components=2)
pc =pca.fit_transform(df)

#print new dimensions
print(pc.shape)
print(pc[:10])

#re-fit kmeans model to the principle components with the approiate number of cluster
kmeans=KMeans(n_clusters=3)

kmeans.fit(pc)

#Visulize high dimensional clusters using PCA

h= 0.02

#generate mesh grid
x_min,x_max=pc[:,0].min() -1,pc[:,0].max()+1
y_min,y_max=pc[:,0].min() -1,pc[:,0].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

Z= kmeans.predict(np.c_[xx.ravel(),yy.ravel()])

#generate color plot from results
Z=Z.reshape(xx.shape)
plt.figure(figsize=(12,12))
plt.clf()
# plt.imshow(Z,interploation='nearest',extent=(xx.min(),xx.max(),yy.min(),yy.max()),cmap=plt.get_cmap('tab20c'),aspect='auto',origin='lower')

#plot the principle component on the color plot
for i,point in enumerate(pc):
    if target[i]==0:
        plt.plot(point[0],point[1],'g.',markersize=10)
    if target[i]==1:
        plt.plot(point[0],point[1],'r.',markersize=10)
    if target[i]==2:
        plt.plot(point[0],point[1],'b.',markersize=10) 


#plot the cluster centroids
centroids= kmeans.cluster_centers_
plt.scatter(centroids[:,0],centroids[:,1],marker = 'x', s = 250, linewidth = 4,
           color = 'w', zorder = 10)

# set plot title and axis limits
plt.title('K-Means Clustering on PCA-Reduced Iris Data Set')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.xticks(())
plt.yticks(())

# display the plot
plt.show()


from sklearn import metrics

#K Means clustering on non reduced data
kmeans1=KMeans(n_clusters=3)
kmeans1.fit(features)

#K Means clustering on a PCA reduced data
kmeans2=KMeans(n_clusters=3)
kmeans2.fit(pc)

#print metrics for non reduced data
print('Non -reduced data')
print('Homogenity: {}'.format(metrics.homogeneity_score(target,kmeans1.labels_)))
print('Completeness: {}'.format(metrics.completeness_score(target,kmeans1.labels_)))
print('V-Measure: {}'.format(metrics.v_measure_score(target,kmeans1.labels_)))


print('PCA reduced data')
print('Homogenity: {}'.format(metrics.homogeneity_score(target,kmeans2.labels_)))
print('Completeness: {}'.format(metrics.completeness_score(target,kmeans2.labels_)))
print('V-Measure: {}'.format(metrics.v_measure_score(target,kmeans2.labels_)))

print(kmeans1.labels_)
print(kmeans2.labels_)
print(target)