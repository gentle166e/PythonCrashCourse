#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/18 Wednesday 15:41:51
@Author     :Le
@LastEditor :
@EditTime   :
'''


import matplotlib.pyplot as plt

values = list(range(1, 1001))
squares = [x ** 2 for x in values]

# plt.plot(values, squares, linewidth=3)

# 绘制点图
# plt.scatter(values, squares, c='red', edgecolors='none', s=1)
# plt.scatter(values, squares, c=(0.5, 0, 0.5), edgecolors='none', s=1)
plt.scatter(values, squares, c=squares, cmap=plt.cm.Reds, edgecolors='none', s=1)

# 设置图表标题，并给坐标轴加上标签
plt.title('square numbers', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)


# 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)

# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('square_plot.png', bbox_inches='tight')
