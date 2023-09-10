import pygame


class Ship:
    """初始化飞船并进行初始设置"""
    def __init__(self, ai_settings, screen):
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
