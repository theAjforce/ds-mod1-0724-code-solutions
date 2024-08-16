import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

data = pd.read_excel("Data_Analysis_Project.xlsx", 'Data')

data['Month ID(YYYYMM)']=pd.to_datetime(data['Month ID(YYYYMM)'], format="%Y%m")

sns.barplot(x= 'Month ID(YYYYMM)', y= 'Defects', data=data)

sns.barplot(x="Month ID(YYYYMM)",y="Opportunities", data=data)

data["defect rate"] = data['Defects']/data['Opportunities']
data['correct mean rate'] = data['Mean Rate']/1000000
data['correct 2 Sigma limit'] = data['2 Sigma limit']/1000000
data['correct 3 Sigma limit'] = data["3 Sigma limit"]/1000000

plt.plot(data["Month ID(YYYYMM)"], data[['defect rate','correct mean rate', 'correct 2 Sigma limit', 'correct 3 Sigma limit']])

plt.plot("Month ID(YYYYMM)", "Defects", data=data)

data.info()

fig, ax1 = plt.subplots()
ax1.set_xlabel("Time")
ax1.set_ylabel("# of Laptops")
ax1.plot("Month ID(YYYYMM)","Defects",color='blue',data=data)
ax1.plot("Month ID(YYYYMM)","Opportunities",color='green',data=data)
ax1.annotate("Opportunities have continued to increase while defects remain low.", xy=(data.loc[22, "Month ID(YYYYMM)"], 3516), xytext=(data.loc[20, "Month ID(YYYYMM)"],2500))
plt.legend(loc='center left')
ax2=ax1.twinx()
ax2.set_ylabel('rate')
ax2.plot("Month ID(YYYYMM)", "defect rate",color='red',data=data)
ax2.plot("Month ID(YYYYMM)", "correct mean rate",color='cyan',data=data)
ax2.plot("Month ID(YYYYMM)", "correct 2 Sigma limit",color='magenta',data=data)
ax2.plot("Month ID(YYYYMM)", "correct 3 Sigma limit",color='yellow',data=data)
ax2.annotate("Defect rate reached 72% on 2016-08-01 :(", xy=(data.loc[1,"Month ID(YYYYMM)"],0.722), xytext=(data.loc[3,"Month ID(YYYYMM)"],0.53),arrowprops=dict(facecolor='black', shrink=0.05))
ax2.annotate("Defect rate was our lowest ever parallel to opportunitis being the highest!", xy=(data.loc[22, "Month ID(YYYYMM)"], 0.038), xytext=(data.loc[13, "Month ID(YYYYMM)"],.15),arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend()