#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/12 Thursday 15:05:09
@Author     :Le
@LastEditor :
@EditTime   :
'''


class Settings():
    '''存储外星人入侵的所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.8

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 50, 0)
        self.bullet_num = 5

        # 外星人设置
        self.alien_speed = 1
        self.aliens_drop_speed = 1
        # aliens_direction为1表示向右移动，为-1表示向左移动
        self.aliens_direction = 1
        # self.alien_num = 8
        self.ship_limit = 3

        # 以什么样的速度加快游戏节奏
        self.speedup = 1.1
        self.score_scale = 1.5

        self.alien_points = 50
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1

        self.aliens_direction = 1


    def increase_speed(self):
        '''提高速度设置和外星人点数'''
        self.ship_speed *= self.speedup
        self.bullet_speed *= self.speedup
        self.alien_speed *= self.speedup
        self.alien_points = int(self.alien_points * self.score_scale)
        # print('aliens points:',self.alien_points)
