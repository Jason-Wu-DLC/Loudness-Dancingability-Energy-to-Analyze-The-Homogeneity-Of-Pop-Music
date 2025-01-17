import pandas as pd
import researchpy as rp


alldata = pd.read_csv('datacleaning.csv',sep=',')


part= alldata.groupby(['year'], as_index=False)[['danceability', 'energy','loudness']].std()


print(rp.correlation.corr_pair(part[['year', 'danceability']]))
print()
print(rp.correlation.corr_pair(part[['year', 'energy']]))
print()
print(rp.correlation.corr_pair(part[['year', 'loudness']]))
print()