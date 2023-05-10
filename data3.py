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
for i in range(10, 1000, 10):
    R_data = pd.read_csv( ".\data3\LLP_3_data_%d_stats.csv" % i, nrows=1, skip_blank_lines=True)
    total_a = total_a.append(R_data)
print(total_a)


plt.plot(total_a['Request Count'], total_a['99%'])
plt.xlabel('Request Count')
plt.ylabel('99%')
plt.title('Line Plot')
plt.show()

# 对 x 和 y 数据进行3次多项式拟合
coefficients = np.polyfit(total_a['Request Count'], total_a['99%'], deg=3)
# 获取拟合函数
fitted_function_frontend = np.poly1d(coefficients)

print(fitted_function_frontend)

# 生成一组新的 x 值
x_new = np.linspace(total_a['Request Count'].min(), total_a['Request Count'].max(), 100)
# 计算对应的 y 值
y_new = fitted_function_frontend(x_new)

# 绘制原始数据和拟合函数的图像
plt.plot(total_a['Request Count'], total_a['99%'], 'o', x_new, y_new, '-')
plt.xlabel('Request Count')
plt.ylabel('99%')
plt.title('Line Plot_er')
plt.legend(['Data', 'Fit'])
plt.show()

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

# 对 x 和 y 数据进行指数函数拟合
coefficients = np.polyfit(total_a['Request Count'], np.log(total_a['99%']), deg=1)

# 获取拟合函数
fitted_function = np.exp(coefficients[1]) * np.exp(coefficients[0] * total_a['Request Count'])
print(fitted_function)

# 生成一组新的 x 值
x_new = np.linspace(total_a['Request Count'].min(), total_a['Request Count'].max(), 100)

# 计算对应的 y 值
y_new = np.exp(coefficients[1]) * np.exp(coefficients[0] * x_new)

# 绘制原始数据和拟合函数的图像
plt.plot(total_a['Request Count'], total_a['99%'], 'o', x_new, y_new, '-')
plt.xlabel('Request Count')
plt.ylabel('99%')
plt.title('Line Plot_e')
plt.legend(['Data', 'Fit'])
plt.show()



def exponential_fit(x_data, y_data):
    # 对 x 和 y 数据进行指数拟合
    coefficients = np.polyfit(x_data, np.log(y_data), deg=2)

    # 获取拟合函数
    fitted_function = lambda x: np.exp(coefficients[1]) * np.exp(coefficients[0] * x)

    return fitted_function
# 定义 x 和 y 数据
x_data = total_a['Request Count']
y_data = total_a['99%']

# 进行指数拟合
fitted_function = exponential_fit(x_data, y_data)

# 打印拟合函数
print(fitted_function)

# 生成一组新的 x 值
x_new = np.linspace(total_a['Request Count'].min(), total_a['Request Count'].max(), 100)

# 计算对应的 y 值
y_new = fitted_function(x_new)

# 绘制原始数据和拟合函数的图像
plt.plot(total_a['Request Count'], total_a['99%'], 'o', x_new, y_new, '-')
plt.xlabel('Request Count')
plt.ylabel('99%')
plt.title('Line Plot_e')
plt.legend(['Data', 'Fit'])
plt.show()