import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pandas series
print("\n--- Pandas Series ---")
series = pd.Series([10, 20, 30, 40],   #values
                   ['A', 'B', 'C', 'D'])   #keys
print(series)
print(series['C'])
print(series[1])

# converting dictionaries
print("\n--- Converting Dictionaries ---")
myDict = {'A':10, 'B':20, 'C':30}
series = pd.Series(myDict,index=['C','A','B'])
print(series)

# pandas data frame
print("\n--- Pandas Data Frame ---")
data = {'Name': ['Anna', 'Bob', 'Charles'],
        'Age': [24, 32, 35],
        'Height': [176, 187, 175]}
df = pd.DataFrame(data)
print(df)
print(df['Name'][1])
print(df[['Name', 'Height']])

# data frame functions
print("\n--- Data Frame Functions ---")
print(df.T)
print(df.dtypes)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.head(2))
print(df.tail(2))

# data frame statistical functions
print("\n--- Data Frame Statistical Functions ---") 
data = {'Name':['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'India'],
        'Age':[24, 32, 35, 45, 22, 54, 55, 43, 25],
        'Height':[176, 187, 175, 182, 176, 189, 165, 187, 167]}
df  = pd.DataFrame(data)
print(df)
print(df['Age'].mean())
print(df['Height'].median())
print(df.mean())
#print(df['Age'].apply(np.sin))

# lambda expressions
print("\n--- Lambda Expressions ---")
print(df['Age'].apply(lambda x: x * 100))

df =  df[['Age', 'Height']]
print(df.apply(lambda x: x.max() - x.min()))

# iterating
print("\n--- Iterating ---")
for x in df['Age']:
    print(x)
print()
for key, value in df.iteritems():
    print("{}: {}".format(key,value))
print()
for index, value in df.iterrows():
    print(index,value)

# sorting
print("\n--- Sorting ---")
df = pd.DataFrame(np.random.rand(10,2),
                  index=[1, 5, 3, 6, 7, 2, 8, 9, 0, 4],
                  columns=['A','B'])
print(df)
print(df.sort_index())
#df.sort_index(inplace=True)

#sort by columns
data = {'Name':['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'India'],
        'Age':[24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height':[176, 187, 175, 182, 176, 189, 165, 187, 167]}
df  = pd.DataFrame(data)
print(df)
df.sort_values(by=['Age','Height'],inplace=True)
print(df)

# joining and merging
print("\n--- Joining and Merging ---")
names = pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Anna', 'Bob', 'Charles', 'Daniel', 'Evan']
})
ages = pd.DataFrame({
    'id':[1,2,3,4,5],
    'age':[20,30,40,50,60]
})
df = pd.merge(names,ages,on='id')
df.set_index('id', inplace=True)
print(df)
print()
# inner join
names = pd.DataFrame({
    'id':[1,2,3,4,5,6],
    'name':['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona']
})
ages = pd.DataFrame({
    'id':[1,2,3,4,5,7],
    'age':[20,30,40,50,60,70]
})
df = pd.merge(names,ages,on='id',how='inner')
df.set_index('id', inplace=True)
print(df)
print()
# left join
df = pd.merge(names,ages,on='id',how='left')
df.set_index('id', inplace=True)
print(df)
print()
# right join
df = pd.merge(names,ages,on='id',how='right')
df.set_index('id', inplace=True)
print(df)
print()
# outer join
df = pd.merge(names,ages,on='id',how='outer')
df.set_index('id', inplace=True)
print(df)
print()

# querying data
print("\n--- Querying Data ---")
data = {'Name':['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'India'],
        'Age':[24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height':[176, 187, 175, 182, 176, 189, 165, 187, 167]}
df  = pd.DataFrame(data)
print(df)
print(df.loc[df['Age'] == 24])
print(df.loc[(df['Age'] == 24) & (df['Height'] > 180)])
print(df.loc[df['Age'] == 24]['Name'])

# read data from files
print("\n--- Read Data From Files ---")
df =  pd.read_csv('data.csv')
df.set_index('id', inplace=True)
print(df)

data = {'Name':['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'India'],
        'Age':[24, 24, 35, 45, 22, 54, 54, 43, 25],
        'Height':[176, 187, 175, 182, 176, 189, 165, 187, 167]}
df  = pd.DataFrame(data)
#df.to_csv('mydf.csv')
df.sort_values(by=['Age','Height'])
df.hist()
plt.show()

plt.plot(df['Age'], 'b-', label="Age")
plt.plot(df['Height'], 'r-', label="Height")
plt.legend(loc='center right')
plt.show()

plt.plot(df['Age'], 'bo')
plt.show()
