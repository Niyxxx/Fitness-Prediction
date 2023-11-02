import pandas as pd

myDF = pd.read_csv('data.csv')
myDF.dropna(inplace= True)
print(myDF)