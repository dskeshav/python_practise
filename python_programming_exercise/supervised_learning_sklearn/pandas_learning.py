import pandas as pd
import numpy as np

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

print('dataframes types \n',df2.dtypes)
print(df2)
dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df.head())
print(df.tail(3))

print('df.index: ',df.index)
print('\ndf.columns:\n',df.columns)

print('\ndf.values:\n',df.values)

print('\ndf.describe:\n',df.describe())

print('\ndf transpose:\n',df.T)

print(df.sort_index(axis=1,ascending=False))
print(df.sort_values(by='B'))
print('\ndf[\'A\']:\n',df['A'])

print(df[0:3])
print(df['20180103':'20180105'])
print(df.loc[dates[0]])

print('\ndf.loc[:,[\'A\',\'B\']]:\n',df.loc[:,['A','B']])

print('\ndf.iloc[3]:\n',df.iloc[3])

print('\ndf.iloc[3:5,0:2]:\n',df.iloc[3:5,0:2])

print('\ndf.iloc[1:3,:]\n',df.iloc[1:3,:])

print('\ndf.iloc[:,1:3]:\n',df.iloc[:,1:3])

print('\ndf.iat[]:\n',df.iat[1,1])

print('\ndf.A>0:\n',df.A>0)
print('\ndf[df.A>0]:\n',df[df.A>0])

print('\ndf[df>0]:',df[df>0])


df3=df.copy()
df3['E']=['one','one','two','three','four','three']
print(df3)

print(df3[df3['E'].isin(['two','four'])])


s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6,freq='D'),dtype=int)
print('\ns1:\n',s1)

df3['F']=s1
print("\ndf3:\n",df3)

df3.at[dates[0],'A']=0
print("\ndf3:\n",df3)

df3.iat[0,1]=0
print("\ndf3:\n",df3)

df3.loc[:,'D']=np.array([5]*len(df))
print("\ndf3:\n",df3)

df4=df3.copy()
df4[df4>0]=-df4

print("\ndf4:\n",df4)