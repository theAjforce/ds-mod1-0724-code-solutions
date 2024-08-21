import pandas as pd
data = pd.read_csv("titanic.csv")

data['age_median'] = data['Age'].transform(lambda x: x.fillna(x.median()))  
data['age_median'].isna().sum()

data['age_mean'] = data.groupby('Sex')['Age'].transform(lambda x: x.fillna(x.mean()))
data['age_mean'].isna().sum()

cabin_sample = data.loc[data['Cabin'].notna(),'Cabin'].sample(687, replace=True)
data.loc[data['Cabin'].isna(),'Cabin'] = cabin_sample.values
data['Cabin'].isna().sum()
#I chose the method above because I felt it gave the data set the most effective distribution of categorical data. 
#Because had I chosen another method it may have replaced the null values with the same cabin and would be heavily biased.
#But with a random distribution of the cabins we get a somewhat even spread of values among the rows.

#Why is it important to handle null values in datasets?

#It is extremely important to handle null values in datasets because null values can create bias when not handled correctly.

