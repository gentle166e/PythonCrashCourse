#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/23 Monday 10:53:12
@Author     :Le
@LastEditor :
@EditTime   :
'''


import matplotlib.pyplot as plt

from random_walk import RandomWalk

for n in range(2):
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # plt.figure(dpi=128, figsize=(10, 6))

    point_num = list(range(rw.num_points))

    # plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(rw.x_values, rw.y_values, c=point_num,
                cmap=plt.cm.cool, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='blue', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)

    plt.title('RandomWalk numbers')
    plt.xlabel('values')
    plt.ylabel('results')
    plt.show()
