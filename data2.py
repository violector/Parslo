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
#total_a.to_csv('total_a.csv', index=False)

# df_even = total_a.iloc[1::2, :]
# df_odd = total_a.iloc[::2, :]
# print(df_odd)
# print(df_even)

plt.plot(total_a['Request Count'], total_a['99%'])
plt.xlabel('Request Count')
plt.ylabel('99%')
plt.title('Line Plot')
plt.show()



def LLP_func_front(x_data, y_data, degree):
    # 对 x 和 y 数据进行一次多项式拟合
    coefficients = np.polyfit(x_data, y_data, deg=degree)

    # 获取拟合函数
    fitted_function = np.poly1d(coefficients)

    return fitted_function

x_data = total_a['Request Count']
y_data = total_a['99%']
degree = 3
y = LLP_func_front(total_a['Request Count'], total_a['99%'], 3)
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

# # 对 x 和 y 数据进行指数函数拟合
# coefficients = np.polyfit(total_a['Request Count'], np.log(total_a['99%']), deg=1)

# # 获取拟合函数
# fitted_function = np.exp(coefficients[1]) * np.exp(coefficients[0] * total_a['Request Count'])
# print(fitted_function)

# # 生成一组新的 x 值
# x_new = np.linspace(total_a['Request Count'].min(), total_a['Request Count'].max(), 100)

# # 计算对应的 y 值
# y_new = np.exp(coefficients[1]) * np.exp(coefficients[0] * x_new)

# # 绘制原始数据和拟合函数的图像
# plt.plot(total_a['Request Count'], total_a['99%'], '-', x_new, y_new, '-')
# plt.xlabel('Request Count')
# plt.ylabel('99%')
# plt.title('Line Plot_e')
# plt.legend(['Data', 'Fit'])
# plt.show()

# # 定义指数函数
# def exp_func(x, a, b, c):
#     return a * np.exp(-b * x) + c

# # 拟合数据
# popt, pcov = curve_fit(exp_func, total_a['Request Count'], total_a['99%'])

# # 生成新的 x 和 y 数据
# x_new = np.linspace(total_a['Request Count'].min(), total_a['Request Count'].max())
# y_new = exp_func(x_new, *popt)

# # 绘制原始数据和拟合函数的图像
# plt.plot(total_a['Request Count'], total_a['99%'], 'o', x_new, y_new, '-')
# plt.xlabel('Request Count')
# plt.ylabel('99%')
# plt.title('Line Plot')
# plt.legend(['Data', 'Fit'])
# plt.show()

plt.plot(total_a['Request Count'], total_a['99.99%'])
plt.xlabel('Request Count')
plt.ylabel('99.99%')
plt.title('Line Plot')
plt.show()

plt.plot(total_a['Request Count'], total_a['Average Response Time'])
plt.xlabel('Request Count')
plt.ylabel('Average Response Time')
plt.title('Line Plot')
plt.show()

plt.plot(total_a['Requests/s'], total_a['99.99%'])
plt.xlabel('Requests/s')
plt.ylabel('99%')
plt.title('Line Plot')
plt.show()

# 生成散点图
plt.scatter(total_a['Request Count'], total_a['99%'])
plt.xlabel('Request Count')
plt.ylabel('latency')
plt.title('scatter Plot')
plt.show()

# # 定义拟合函数
# def func(x, a, b, c):
#     return a * np.exp(b * x) + c

# # 进行拟合
# popt, pcov = curve_fit(func, total_a['Request Count'], total_a['99%'])

# # 输出拟合系数
# print(popt)

# # 绘制曲线
# plt.plot(total_a['Request Count'], total_a['99%'], label='data')
# plt.plot(total_a['Request Count'], func(total_a['Request Count'], *popt), 'r-', label='fit')
# plt.legend()
# plt.show()