import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datacleaning.csv',sep=',')

group= data.groupby(['year'], as_index=False)[['danceability', 'energy','loudness']].std()


group_mean = data.groupby(['year'], as_index=False)[['danceability','energy','loudness']].mean()

plt.plot(group['year'], group['danceability'], label="Danceability's SD")

plt.plot(group_mean['year'], group_mean['danceability'], label="Danceability's Mean")
plt.legend()
plt.tight_layout()
plt.savefig('danceability-M.pdf')
