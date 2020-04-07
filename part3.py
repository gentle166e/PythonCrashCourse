#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/09 Monday 11:05:50
@Author     :Le
@LastEditor :
@EditTime   :
'''

# from module_name import function_0, function_1, function_2 
# from module_name import function_name as fn 


def show_break():
    print('-x-' * 20)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

sort_cars = sorted(cars, reverse=True)
cars.reverse()
print(sort_cars, cars, cars, cars[-1])

for car in cars:
    print('the name of the car is:'.title() + car.title())

print('the value of range(3, 8) is: '.title())
for value in range(3, 8):
    print(value, end=' ')
print('\n', type(range(1, 5)))

squares = [value ** 2 for value in range(2, 6)]
print('the squares is:'.title(), squares)
for num in squares:
    print(num, end=' ')
print(squares[:2])

dic_1 = {}
dic_1['color'] = 'red'
dic_1['points'] = 5
dic_1['age'] = 18
print(dic_1)
dic_1['color'] = ['green', 'yellow', 'gray']
dic_1['name'] = {'li': 'lily', 'Ja': 'jack'}
# del dic_1['age']
print('dic_1 is:', dic_1)
show_break()
# 遍历字典的键
for k in sorted(dic_1):  # 遍历字典时会默认遍历所有的键，因此等效于： for k in dic_1.keys():
    print(f'key: {k}')
    print(f'value: {dic_1[k]}')
show_break()
# 遍历字典的值
for v in dic_1.values():
    print(f'value: {v}')
show_break()
# 遍历字典的键值对
for k, v in dic_1.items():
    print(f'key: {k}')
    print(f'value: {v}')


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car():

    def __init__(self):
        super().__init__()  # 这行代码让此类实例包含父类的所有属性


filename = r'D:\project\PythonProject\Booktest\rumendaoshijian\pi.txt'
with open(filename) as p:
    lines = p.readlines()

nlines = []
pi_str = ''
for line in lines:
    pi_str += line.strip()
    nlines.append(line.rstrip())
    print(line.rstrip())

print(lines, nlines, pi_str, len(pi_str))

writef = 'try.txt'
with open(writef, 'w') as w:
    w.write('I am programming.\n')
    w.write('I love programming.\n')

with open(writef) as w:
    content = w.read()
    print(content)


def count_words(filename):
    '''计算一个文件大概包含多少个单词'''
    words = ''
    try:
        with open(filename) as fn:
            content = fn.read()
            words = content.split()
    except FileNotFoundError:
        print(f'sorry, the file {filename} does not exist!')
    else:
        # print(len(words), len(content), type(content.split()))
        print(f'the {filename} has about {len(words)} words.')


filenames = ['little women.txt', 'ion.txt', 'goook.txt', 'emma.txt']
for filename in filenames:
    count_words(filename)


import json

nums = [2, 3, 5, 7, 9, 11]
filename = 'nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f)  # 存储数据

with open(filename) as f:
    numb = json.load(f)  # 读取数据
print(numb)