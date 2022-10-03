import random

import numpy as np
a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])
C = a*2
D = b*2
# print(C)
# print(D)
# print(C[0:2])
# print(D[0:2])
e = [[1, 2], [3, 4], [5, 6]]
f = np.array([[1, 2], [3, 4], [5, 6]])
# print(e)
# for i in f:
#     print(i)
#     # print(type(i))
# x = np.arange(6)
# x1 = np.arange(1, 3)
# x2 = np.arange(1, 3, 0.5)
# print(x)
# print(x1)
# print(x2)
# for i in range(3):
#     a = np.random.randn(3)
#     b = np.random.rand(3)
#     print(a)
#     print(b)
x3 = np.random.rand(25).reshape(5, 5)
# print(x3)


import pandas as pd
s1 = pd.Series(['丁一', '王二', '张三'])
# print(s1)
s2 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['data', 'score'], index=['A', 'B', 'C'])
l1 = [1, 3, 5]
l2 = [2, 4, 6]
s3 = pd.DataFrame({'a': l1, 'b': l2}, index=['x', 'y', 'z'])
print(s3)
print(s3.T)
#delimiter 用于指定CSV中的分隔符号，默认为逗号
#sheet_name 第几个工作表
data = pd.read_csv('E:\PyDemo\PythonSpider\北京新发地每日菜价.csv', delimiter=',', encoding="utf-8")
print(data.head(5))

a1 = data['品名'][0:5]
# print(a1)

a2 = data[['品名', '最低价']][0:5]
# print(a2)

#iloc根据行序号选取
a3 = data.iloc[0:5]
print(a3)
a4 = data[(data['品名'] == '大白菜') & (data['最低价'] >= 0.1)]
# a5 = data[(data['品名'] == '大白菜') & (data['最低价'] > 0.9) & (data['发布日期'] == '2022-08-29 00:00:00')]
# print(a4)
# print(a5)
# DF = pd.DataFrame
# a4.to_csv('E:\PyDemo\数据分析\大白菜菜价.csv', index=None)
# print('写入完成！')
#shape 快速查看整体行数列数
# print(a4.shape)
# print(a4.describe())
#value_counts 快速查看某个数据出现次数
# print(a4['最低价'].value_counts())

a5 = data['最高价'] - data['最低价']
# print(a5.head(5))

#数据排序
a6 = a4.sort_values(by='最低价', ascending=False)
print(a6)