import matplotlib.pyplot as plt
import seaborn as sns
import pandas
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split

games=pandas.read_csv("games.csv")

print('shape:',games.shape)
print('before:',games.columns)
plt.hist(games['average_rating'])
plt.show()

games=games[games["users_rated"] > 0]
games=games.dropna(axis=0)

print(games.columns)
print(games.shape)
plt.hist(games['average_rating'])
plt.show()

#Get all the columns from the dataframe
columns= games.columns.tolist()

#filter the columns to raemaove data we do not want
columns=[c for c in columns if c not in ['bayes_average','average_rating','type','name','id']]

#Store the variable we'll be predicting on
target="average_rating"


#Coreleation matrix
corrmat=games.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()

#generate training set
train= games.sample(frac=0.8,random_state=1)

#Selecting anything not in the training set
test=games.loc[~games.index.isin(train.index)]

print(train.shape," ",test.shape)

#Import liner regression model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

LR=LinearRegression()
LR.fit(train[columns],train[target])

predictions=LR.predict(test[columns])

mean_squared_error(predictions,test[columns])

