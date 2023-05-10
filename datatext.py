import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#file_path = "C:\Users\Siat-H\Desktop\Parslo_LLP\locust\\"
res = []
average = []
arrival = []

total_a = pd.DataFrame()

# 统计出所有 arrival rate 下的平均延迟

total_a = pd.read_csv( ".\datatext\LLP_stats_history.csv" , skip_blank_lines=True)

    

print(total_a)
# df_even = total_a.iloc[1::2, :]
# df_odd = total_a.iloc[::2, :]
# print(df_odd)
# print(df_even)
#df = df[~df['身高'].isin([160])]

#total_a = total_a[~total_a['Failures/s'].isin([0])]

plt.plot(total_a['Total Request Count'], total_a['99%'])
plt.xlabel('Request Count')
plt.ylabel('latency')
plt.title('Line Plot')
plt.show()

plt.plot(total_a['Total Request Count'], total_a['99%'],total_a['Total Average Response Time'])
plt.xlabel('Total Request Count')
plt.ylabel('latency')
plt.title('Line Plot')
plt.show()

plt.plot(total_a['Timestamp'], total_a['99%'],total_a['Total Average Response Time'])
plt.xlabel('Timestamp')
plt.ylabel('latency')
plt.title('Line Plot')
plt.show()
# 生成散点图
plt.scatter(total_a['Total Request Count'], total_a['99.99%'])
plt.xlabel('Request Count')
plt.ylabel('latency')
plt.title('scatter Plot')
plt.show()