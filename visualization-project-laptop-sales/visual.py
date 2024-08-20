import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Sales_data.txt') 

gender_count = data['Contact Sex'].value_counts()
plt.bar(gender_count.index, gender_count.values)
plt.xlabel('Contact Sex')
plt.ylabel('Count')

gender_total_profit = data.groupby('Contact Sex')['Profit'].sum()
plt.bar(gender_total_profit.index, gender_total_profit.values)
plt.xlabel('Contact Sex')
plt.ylabel('Profit')

gender_total_cost = data.groupby('Contact Sex')['Our Cost'].sum()
plt.bar(gender_total_cost.index, gender_total_cost.values)
plt.xlabel('Contact Sex')
plt.ylabel('Our Cost')

gender_cash_constrained = data.groupby('Contact Sex')['Sale Price'].sum()
plt.bar(gender_cash_constrained.index, gender_cash_constrained.values)
plt.xlabel('Contact Sex')
plt.ylabel('Sale Price')  

age_bin = pd.cut(data['Contact Age'],11)
data['age_bins'] = age_bin
age_profit = data.groupby('age_bins')['Profit'].sum()
age_profit.plot(kind='bar', xlabel= "Age Bins", ylabel="Profit (Sum)")

product_profit = data.groupby('Product ID')['Profit'].sum()
plt.bar(product_profit.index, product_profit.values)
plt.xlabel('Product ID')
plt.ylabel('Profit')

lead_source_profit = data.groupby('Lead Source')['Profit'].sum()
plt.bar(lead_source_profit.index, lead_source_profit.values)
plt.xlabel('Lead Source')
plt.ylabel('Profit')

best_month = data.groupby('Sale Month')['Profit'].sum()
plt.bar(best_month.index, best_month.values)
plt.xlabel('Sale Month')
plt.ylabel('Profit')