#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/12 Thursday 15:30:14
@Author     :Le
@LastEditor :
@EditTime   :
'''


import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    '''对飞船进行管理的类'''

    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置--放在屏幕底部中央'''
        super(Ship, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien/images/ship.bmp')
        # self.image = pygame.image.load('alien/images/bt.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_left = False
        self.moving_right = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx