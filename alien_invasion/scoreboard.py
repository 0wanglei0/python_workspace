import pygame.font
from pygame.sprite import Group

from ships import Ship


class Scoreboard:
    """显示得分的类"""

    def __init__(self, ai_settings, screen, stats):
        self.all_ships = Group()
        self.level_rect = None
        self.level_image = None
        self.high_score_image = None
        self.high_score_rect = None
        self.score_image = None
        self.score_rect = None
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # round_score = round(self.stats.score, -1)
        round_score = self.stats.score
        score_str = "Score: {:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def prep_high_score(self):
        # round_high_score = round(self.stats.high_score, -1)  # 四舍五入
        round_high_score = self.stats.high_score
        high_score_str = "High Score: {:,}".format(round_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.all_ships.draw(self.screen)

    def prep_level(self):
        self.level_image = self.font.render(f"Level: {self.stats.level} ", True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.left - 10
        self.level_rect.top = self.score_rect.top

    def prep_ships(self):
        self.all_ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.all_ships.add(ship)
