#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/26 Thursday 16:17:34
@Author     :Le
@LastEditor :
@EditTime   :
'''


from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
import pygal

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
       'gy', 'pe', 'py', 'sr', 'uy', 've'])


wm.render_to_file('americas.svg')

for county_code in sorted(COUNTRIES.keys()):
    print(county_code, COUNTRIES[county_code])
