import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#file_path = "C:\Users\Siat-H\Desktop\Parslo_LLP\locust\data1\\"
res = []
average = []
arrival = []

total_a = pd.DataFrame()
df_even = pd.DataFrame()
df_odd = pd.DataFrame()
# 统计出所有 arrival rate 下的平均延迟
for i in range(10, 510, 10):
    R_data = pd.read_csv( ".\data1\LLPdata%d_stats.csv" % i, nrows=1, skip_blank_lines=True)
    total_a = total_a.append(R_data)
    

print(total_a)
# df_even = total_a.iloc[1::2, :]
# df_odd = total_a.iloc[::2, :]
# print(df_odd)
# print(df_even)

plt.plot(total_a['Request Count'], total_a['99%'])
plt.xlabel('Request Count')
plt.ylabel('latency')
plt.title('Line Plot')
plt.show()

# 生成散点图
plt.scatter(total_a['Request Count'], total_a['99%'])
plt.xlabel('Request Count')
plt.ylabel('latency')
plt.title('scatter Plot')
plt.show()