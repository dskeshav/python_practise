import matplotlib.pyplot as plt
import seaborn as sns
import pandas
from sklearn.model_selection import train_test_split


games=pandas.read_csv("games.csv")

print('shape:',games.shape)
print('before:',games.columns)
# plt.hist(games['average_rating'])
# plt.show()

#print the first row of all the games with zero scores
print(games[games["average_rating"]==0].iloc[0])

#print the first row of games with scores greater than 0
print(games[games["average_rating"]>0].iloc[0])

games=games[games["users_rated"] > 0]
games=games.dropna(axis=0)

print(games.columns)
print(games.shape)
plt.hist(games['average_rating'])
plt.show()

#Get all the columns from the dataframe
columns= games.columns.tolist()

#filter the columns to remove data we do not want
columns=[c for c in columns if c not in ['bayes_average','average_rating','type','name','id']]
print("Columns: ",columns)
#Store the variable we'll be predicting on
target="average_rating"


#Coreleation matrix
corrmat=games.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)
plt.show()

#generate training and test datasets
from sklearn.model_selection import train_test_split

#generate training set
train= games.sample(frac=0.8,random_state=1)

#Selecting anything not in the training set and put in test set
test=games.loc[~games.index.isin(train.index)]

#Print shapes
print(train.shape," ",test.shape)

#Import linear regression model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#initilize the model class
LR=LinearRegression()

# Fit the model class
LR.fit(train[columns],train[target])

#Generate predictions for test set
predictions=LR.predict(test[columns])

# Compute error between our test predictions
msr=mean_squared_error(predictions,test[target])
print("mean square error: ",msr)


#Import the randomforest  model
from sklearn.ensemble import RandomForestRegressor

#Initilize the model
RFR=RandomForestRegressor(n_estimators=100,min_samples_split=10,random_state=1)

#fit to the data
RFR.fit(train[columns],train[target])

#make predictions
predictions=RFR.predict(test[columns])

#compute the error between test predictions and actual values
msr2=mean_squared_error(predictions,test[target])
print("msr2:",msr2)

print(test[columns].iloc[0])

rating_LR=LR.predict(test[columns].iloc[0].values.reshape(1,-1))
rating_RFR =RFR.predict(test[columns].iloc[0].values.reshape(1,-1))

print("LR rating: ",rating_LR)
print("RFR rating: ",rating_RFR)

# get the target values
print(test[target].iloc[0])
