import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler
import numpy as np
from scipy.stats import yeojohnson
from sklearn.preprocessing import normalize

df = pd.read_csv("mtcars_mod.csv")

scaler_maxabs = MaxAbsScaler()
hp_df = df[['hp']]
scaler_maxabs.fit(hp_df)
scaler_maxabs.transform(hp_df)

scaler_minmax = MinMaxScaler()
disp_df = df[["disp"]]
scaler_minmax.fit(disp_df)
scaler_minmax.transform(disp_df)

scaler_robust = RobustScaler()
drat_df = df[["drat"]]
scaler_robust.fit(drat_df)
scaler_robust.transform(drat_df)

scaler_standard = StandardScaler()
wt_df = df[["wt"]]
scaler_standard.fit(wt_df)
scaler_standard.transform(wt_df)

mpg_yj, mpg_lambda = yeojohnson(df['mpg'])

num_df = df.iloc[:, 1:]
normal_data = normalize(num_df, norm="l2")
df.loc[:, 1:] = normal_data


'''
QUIZ
1.Which scaling method works best for data with outliers?
Robust scaling
2.Which scaling method produces data that is normally distributed? What is its mean and variance?
Standard scaling, the mean is the population mean and the variance is 1.
3.Which scaling method does not remove sparsity? What is sparsity?
MaxAbs Scaling, sparsity is when many values are 0.
4.Which scaling method is best to use if the bounds of your data are known from domain knowledge?
MinMax Scaling
'''