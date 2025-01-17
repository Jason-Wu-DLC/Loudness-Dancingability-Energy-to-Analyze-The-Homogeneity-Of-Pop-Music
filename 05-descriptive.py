
import pandas as pd


alldata = pd.read_csv('datacleaning.csv',sep=',')

print(alldata['danceability'].describe())
print()
print(alldata['energy'].describe())
print()
print(alldata['loudness'].describe())