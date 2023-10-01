import sys
import pygame

from button import Button
from ships import Ship  # 先from再import
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


class Settings:
    """存储外星人入侵所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

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

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化pygame
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200, 800))  # 屏幕此处必须是tuple()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 屏幕此处必须是tuple()
    pygame.display.set_caption("Alien Invasion")  # 设置标题
    # bg_color = (230, 230, 230)

    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    game_stats = GameStats(ai_settings)
    while True:
        # 监听键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # gf.check_events()
        gf.check_events(ai_settings, screen, ship, aliens, bullets, game_stats, play_button)
        if game_stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, game_stats, screen, ship, aliens, bullets)
        # 每次循环都重绘屏幕,填充背景颜色
        # screen.fill(bg_color)
        # screen.fill(ai_settings.bg_color)
        # # 屏幕展示， 在此处无限刷新，更新屏幕，营造平滑移动的效果
        # ship.blit_me()
        # pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, game_stats, play_button)


if __name__ == "__main__":
    run_game()


