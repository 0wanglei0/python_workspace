import sys

import pygame
from pygame.sprite import Sprite, Group

"""
1.雨滴
rect y

check_edge

create多个

"""


class Settings:
    """存储外星人入侵所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 250
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1 表示向右移，为-1表示向左移
        self.fleet_direction = 1


class Ship(Sprite):
    """初始化飞船并进行初始设置"""
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # print(self.rect.centerx)
        # 将每艘新飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx  # 是外接矩形的中心点x坐标
        self.rect.bottom = self.screen_rect.bottom  # 对其方式
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        # 此处不使用elif是因为要让所有按键都处于同一优先级进行，如果使用elif，则默认右键优先
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center  # centerx只能使用整数值，因此赋值时只能保存center的整数部分

    def blit_me(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


class Rain(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = self.rect.width
        self.y = self.rect.height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.fleet_drop_speed = 1
        self.fleet_direction = 1
        self.color = 0, 0, 250

    def check_edges(self):
        if self.y > self.screen.get_height():
            return True

    def update(self):
        self.y += self.fleet_drop_speed * self.fleet_direction
        self.rect.y = self.y
        pygame.draw.rect(self.screen, self.color, self.rect)


def check_rain_edge(rain):
    if rain.check_edges():
        return True


def create_rains(screen, rains):
    for rain_num in range(10):
        rain = Rain(screen)
        rain.x += rain.width * rain_num + 20
        rain.rect.x = rain.x
        rains.add(rain)
    return rains


def start_rain():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("下雨啦")

    rains = Group()
    create_rains(screen, rains)
    ai_settings = Settings()
    ship = Ship(ai_settings, screen)
    ships = Group()
    print(type(ship))
    ships.add(ship)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for rain in rains:
            if check_rain_edge(rain):
                rains.remove(rain)
            if len(rains) != 0:
                rain.update()
            else:
                create_rains(screen, rains)
        collisions = pygame.sprite.groupcollide(ships, rains, False, True)

        screen.fill((230, 230, 230))
        rains.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    start_rain()
