#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/13 Friday 10:48:26
@Author     :Le
@LastEditor :
@EditTime   :
'''


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''对子弹进行管理的类'''

    def __init__(self, ai_settings, screen, ship):
        '''在飞船所处的位置创建一个子弹对象'''
        # Bullet类继承了我们从模块pygame.sprite中导入的Sprite类。通过使用精灵，
        # 可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
        # super(Bullet, self).__init__()  # python2.7语法
        super().__init__()  # python3语法
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y -= self.speed
        # 更新表示子弹rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
