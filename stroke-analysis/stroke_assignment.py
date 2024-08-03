import pandas as pd
stroke = pd.read_csv('healthcare-dataset-stroke-data.csv')
stroke.describe() #1
stroke_floats = stroke.select_dtypes(include='float64')
stroke_floats.describe()#2
stroke_df = stroke.groupby('stroke')#3
stroke_df.groupby('stroke').get_group(1)#4
stroke_int = stroke.select_dtypes(include='int64')#5
stroke_int.describe(percentiles=[])#6
stroke_hyp_dis = stroke.groupby(["hypertension","heart_disease"])#7
stroke[(stroke.hypertension == 1) & (stroke.heart_disease == 1)]#8
hyper_true = stroke.hypertension == 1 #9
heart_true = stroke.heart_disease ==1 #9
count_hyper = hyper_true['id'].nunique() #9
count_heart = heart_true['id'].nunique() #9
count = count_hyper + count_heart #9
stroke_hyp_dis['stroke'].agg(["mean","std"]) #10