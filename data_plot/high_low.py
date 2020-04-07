#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/24 Tuesday 10:35:43
@Author     :Le
@LastEditor :
@EditTime   :
'''


import csv

from matplotlib import pyplot as plt
from datetime import datetime


def check_error():
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
    except ValueError as v:
        print(current_date, v, 'missing date')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


filename = 'sitka_weather_07-2018.csv'
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        # for index, column_header in enumerate(header_row):
        #     # 用enumerate来获取每个元素的索引及其值
        #     print(index, column_header)
        dates, highs, lows = [], [], []
        for row in reader:
            # current_date = datetime.strptime(row[2], r'%Y-%m-%d')
            # dates.append(current_date)
            # high = int(row[5])
            # low = int(row[6])
            # highs.append(high)
            # lows.append(low)
            check_error()
        print(highs)
except FileNotFoundError as e:
    print(f'there is somethings wrong:{e}')

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(8, 5))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha用于指定透明度， 0：完全透明，1：完全不透明
plt.plot(dates, lows, c='green', alpha=0.9)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)


# 设置图形的格式
title_str = 'daily high temperatures'.capitalize()
plt.title(title_str, fontsize=24)
plt.xlabel('day', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
