import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datacleaning.csv',sep=',')

group= data.groupby(['year'], as_index=False)[['danceability', 'energy','loudness']].std()


group_mean = data.groupby(['year'], as_index=False)[['danceability','energy','loudness']].mean()

plt.plot(group['year'], group['loudness'], label="Loudness's SD")
plt.plot(group_mean['year'], group_mean['loudness'], label="Loudness's Mean")
plt.legend()
plt.tight_layout()
plt.savefig('loudness-M.pdf')