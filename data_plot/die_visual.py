#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/23 Monday 16:12:01
@Author     :Le
@LastEditor :
@EditTime   :
'''


import pygal
from die import Die


# 创建一个D6
die1 = Die()
die2 = Die(10)

# 掷骰子，并将结果存在一个列表中
results = []
for r in range(5000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = {}

max_result = max(results)
min_result = min(results)
for value in range(min_result, max_result + 1):
    frequency = results.count(value)
    frequencies.update({value: frequency})
print(results)
print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 5000 times.'
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = list(range(min_result, max_result+1))
# hist.y_labels = 'results'
hist.x_title = 'result'
hist.y_title = 'frequency of result'
print(frequencies.values())
values = []
for value in frequencies.values():
    values.append(value)
hist.add('D6 + D10', values)
hist.render_to_file('die_visual.svg')
