#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/12 Thursday 20:51:46
@Author     :Le
@LastEditor :
@EditTime   :
'''


import sys
from time import sleep
import random

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown(event, ai_settings, screen, ship, bullets):
    '''响应按键按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        print('player quit')
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    # 如果还未达到极限就发射一颗子弹
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) <= ai_settings.bullet_num:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup(event, ship):
    '''响应松开按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_bt, ship, aliens, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_bt, 
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_bt,
                      ship, aliens, bullets, mouse_x, mouse_y):
    # 玩家单击按钮时开始新游戏
    button_clicked = play_bt.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_aliens(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, 
                  aliens, bullets, play_bt):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    # 如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_bt.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''响应子弹和外星人的碰撞'''
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        # 删除现有子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_aliens(ai_settings, screen, ship, aliens)


def check_high_scores(stats, sb):
    '''检查是否诞生了最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def get_num_x(ai_settings, alien_width):
    # 计算每行可容纳多少个外星人
    avaliable_space = ai_settings.screen_width
    alien_num = int(avaliable_space / (2 * alien_width))
    return alien_num


def get_num_y(ai_settings, ship_height, alien_height):
    # 计算屏幕可容纳多少行外星人
    avaliable_space_y = (
        ai_settings.screen_height - (1 * alien_height) - ship_height
        )
    alien_num_y = int(avaliable_space_y / (2 * alien_height))
    return alien_num_y


def create_alien(ai_settings, screen, aliens, alien_n, y_n):
    '''创建一个外星人并将其放在当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_n + random.random() * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * y_n
    aliens.add(alien)


def create_aliens(ai_settings, screen, ship, aliens):
    # 创建外星人群
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_num = get_num_x(ai_settings, alien.rect.width)
    y_n = get_num_y(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_y in range(y_n):
        for alien_n in range(alien_num):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_n, row_y)


def get_max_x(aliens):
    '''获取最大右坐标'''
    rect_x = []
    for alien in aliens.sprites():
        rect_x.append(alien.rect.right)
    if len(rect_x) > 0:
        return max(rect_x)
    else:
        return 0


def get_min_x(aliens):
    '''获取最小左坐标'''
    rect_x = []
    for alien in aliens.sprites():
        rect_x.append(alien.rect.left)
    if len(rect_x) > 0:
        return min(rect_x)
    else:
        return 0


def check_aliens_edges(ai_settings, screen, aliens):
    '''有外星人到达边缘时采取措施'''
    # for alien in aliens.sprites():
        # if alien.check_edges():
            # change_aliens_direction(ai_settings, aliens)
            # break
    if len(aliens) > 0:
        if get_max_x(aliens) >= screen.get_rect().right:
            change_aliens_direction(ai_settings, aliens)
        elif get_min_x(aliens) <= 0:
            change_aliens_direction(ai_settings, aliens)
    else:
        pass


def change_aliens_direction(ai_settings, aliens):
    '''将整群外星人下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.aliens_drop_speed
    ai_settings.aliens_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left > 0:
        # 将ship_left减去1
        stats.ships_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_aliens(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''检查是否有外星人到达了屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''检查所有外星人是否位于屏幕边缘，更新外星人群中所有外星人的位置'''
    check_aliens_edges(ai_settings, screen, aliens)
    aliens.update()

    # 检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
        print('YEAH, HIT!')

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
