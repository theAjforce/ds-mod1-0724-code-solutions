import pandas as pd

entry_data = pd.read_csv("event_type.csv")
log_data = pd.read_csv("log_feature.csv")
resource_data = pd.read_csv("resource_type.csv")
severity_data = pd.read_csv("severity_type.csv")
train_data = pd.read_csv("train.csv")
datas = [entry_data, log_data, resource_data, severity_data, train_data]

first_merge = pd.merge(entry_data, log_data, on='id', how= 'inner')
second_merge = pd.merge(first_merge, resource_data, on='id', how='inner')
third_merge = pd.merge(second_merge, severity_data, on='id', how='inner')
final_merge = pd.merge(third_merge, train_data, on='id', how='inner')

final_merge1 = final_merge[:30000]
final_merge2 = final_merge[30000:]
final_merge3 = pd.concat([final_merge1,final_merge2])

final_merge3.drop_duplicates()