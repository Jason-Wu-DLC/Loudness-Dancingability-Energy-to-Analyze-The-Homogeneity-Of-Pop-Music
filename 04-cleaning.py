# Step Read
import pandas as pd

# Step Read the data
dataclean = pd.read_csv('spotify_audiofeatures.csv',sep=',')
 
# Step Get an overview of the variables
print(dataclean.info())

print(dataclean.shape) 
print()



# StepPrint and clean missing data
print('\n # Missing data:\n', dataclean.isnull().sum())
isolatemissing = pd.isnull(dataclean['trackid'])
print('\n Rows with missing data:\n', dataclean[isolatemissing])
dataclean = dataclean.dropna()
print('\nDF after:\n', dataclean)

savedata = pd.DataFrame(dataclean) 

savedata.to_csv('cleaningdata.csv',sep=',',index=False)