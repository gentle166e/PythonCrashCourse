#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/26 Thursday 10:50:36
@Author     :Le
@LastEditor :
@EditTime   :
'''


import json
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle


def get_country_code(country_name):
    '''根据指定的国家，返回pygal使用的两个字母的国别码'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        else:
            pass
    # print('wrong')


print(get_country_code('China'))

# 将数据加载到一个列表中
filename = 'population.json'
with open(filename) as f:
    pop_data = json.load(f)
    print(pop_data[0])

# 创建一个包含人口数量的字典
cc_populations = {}

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            # print('error-', country_name)
            pass
    else:
        pass

# 根据人口数量将所有国家分为3组
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop
print(len(cc_pops1), len(cc_pops2), len(cc_pops3))

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'world population in 2010, by country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)

wm.render_to_file('world_population.svg')
