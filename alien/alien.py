#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/13 Friday 16:13:07
@Author     :Le
@LastEditor :
@EditTime   :
'''


import random
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''管理外星人的类'''
    def __init__(self, ai_settings, screen):
        super().__init__()
        # 初始化外星人，并设置其位置
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载外星人图像，并获取其外接矩形
        self.image = pygame.image.load('alien/images/alien1.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width * random.random()
        self.rect.y = 0
        # self.rect.y = self.rect.height * random.random()

        # 储存外星人准确位置
        self.x = float(self.rect.x)

        # self.rect.top = self.screen_rect.top
        # self.rect.centerx = ai_settings.screen_width * random.random()

        # self.y = float(self.rect.y)
        # self.speed = ai_settings.alien_speed

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.right <= 0:
            return True

    def update(self):
        # 向右移动外星人
        self.x += self.ai_settings.alien_speed * self.ai_settings.aliens_direction
        self.rect.x = self.x
