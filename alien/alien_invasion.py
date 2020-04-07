#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/12 Thursday 14:52:23
@Author     :Le
@LastEditor :
@EditTime   :
'''


import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建play按钮
    play_bt = Button(ai_settings, screen, 'play')

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_aliens(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_bt,
                        ship, aliens, bullets)

        if stats.game_active:
            # 移动飞船
            ship.update()
            # gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, 
                         aliens, bullets, play_bt)


if __name__ == "__main__":
    run_game()
