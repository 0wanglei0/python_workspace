import pygame
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((480, 640))
pygame.display.set_caption('飞机大战')

# 加载背景图片和飞机图片
background = pygame.image.load('squares_plot.png')
plane = pygame.image.load('images/ship.bmp')
bullet = pygame.image.load('target_file.png')
enemy = pygame.image.load('images/alien.bmp')

# 创建飞机对象，设置初始位置、速度和方向
plane_rect = plane.get_rect()
plane_speed = 5
plane_direction = 1

# 创建敌机对象，设置初始位置、速度和方向
enemy_rect = enemy.get_rect()
enemy_speed = 2
enemy_direction = 'down'

# 创建子弹对象，设置初始位置、速度和方向
bullet_rect = bullet.get_rect()
bullet_speed = 10
bullet_direction = 1

while True:
    # 检测按键事件，根据按键调整飞机和子弹的状态
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                plane_direction = -1
            elif event.key == K_RIGHT:
                plane_direction = 1
            elif event.key == K_UP:
                bullet_direction = 1
            elif event.key == K_DOWN:
                bullet_direction = -1
            elif event.key == K_SPACE:
                bullet_rect.centerx = plane_rect.centerx + plane_rect[0] // 2 - bullet_rect.width // 2
                bullet_rect.centery = plane_rect.centery - bullet_rect.height // 2

    # 更新飞机和子弹的位置，检测是否发生碰撞
    plane_rect = plane_rect.move(plane_speed * abs(plane_direction), 0)
    bullet_rect = bullet_rect.move(bullet_speed * abs(bullet_direction), 0)
    enemy_rect = enemy_rect.move(enemy_speed, 0)
    if enemy_rect.colliderect(plane_rect):
        print('游戏结束')
        pygame.quit()
        sys.exit()
    if bullet_rect.colliderect(enemy_rect):
        enemy_rect.topleft = (enemy_rect[0] - enemy_rect[2], enemy_rect[1] - enemy_rect[3])
        bullet_rect.topleft = (-bullet_rect[0], -bullet_rect[1])
        enemy_speed += 1
        bullet_speed = 10
        bullet_rect = bullet_rect.move(bullet_speed, 0)
        enemy_rect = enemy_rect.move(enemy_speed, 0)
        if enemy_rect.top > screen.get_height():
            enemy_speed += 1
            bullet_speed = 10
            bullet_rect = bullet_rect.move(bullet_speed, 0)
            enemy_rect = enemy_rect.move(enemy_speed, 0)
            enemy_rect.topleft = (enemy_rect[0] - enemy_rect[2], enemy_rect[1] - enemy_rect[3])
            bullet_rect.topleft = (-bullet_rect[0], -bullet_rect[1])
            enemy_speed += 1
            bullet_speed = 10
            bullet_rect = bullet_rect.move(bullet_speed, 0)
            enemy_rect = enemy_rect.move(enemy_speed, 0)
            if enemy_rect.top > screen.get_height():
                print('游戏结束')
                pygame.quit()
                sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(plane, plane_rect)
    screen.blit(enemy, enemy_rect)
    screen.blit(bullet, bullet_rect)
    pygame.display.update()