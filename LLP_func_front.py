import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#file_path = "C:\Users\Siat-H\Desktop\Parslo_LLP\locust\\"
res = []
average = []
arrival = []
total_a = pd.DataFrame()
df_even = pd.DataFrame()
df_odd = pd.DataFrame()

# 统计出所有 arrival rate 下的平均延迟
for i in range(10, 610, 10):
    R_data = pd.read_csv( ".\data2\LLPdata_2%d_stats.csv" % i, nrows=1, skip_blank_lines=True)
    total_a = total_a.append(R_data)
print(total_a)

def LLP_func_front():
    # 对 x 和 y 数据进行一次多项式拟合
    coefficients = np.polyfit(total_a['Request Count'], total_a['99%'], deg=3)

    # 获取拟合函数
    fitted_function = np.poly1d(coefficients)

    return fitted_function

# x_data = total_a['Request Count']
# y_data = total_a['99%']
# degree = 3
y = LLP_func_front()
print(y)
# # 对 x 和 y 数据进行一次多项式拟合
# coefficients = np.polyfit(total_a['Request Count'], total_a['99%'], deg=3)

# # 获取拟合函数
# fitted_function = np.poly1d(coefficients)

# print(fitted_function)

# 生成一组新的 x 值
x_new = np.linspace(total_a['Request Count'].min(), total_a['Request Count'].max(), 100)

# 计算对应的 y 值
y_new = y(x_new)

# 绘制原始数据和拟合函数的图像
plt.plot(total_a['Request Count'], total_a['99%'], 'o', x_new, y_new, '-')
plt.xlabel('Request Count')
plt.ylabel('99%')
plt.title('Line Plot_er')
plt.legend(['Data', 'Fit'])
plt.show()