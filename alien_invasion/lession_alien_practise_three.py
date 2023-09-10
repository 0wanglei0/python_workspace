import sys

import pygame

"""
侧面射击：将飞船放在屏幕左边，并可以上下移动，在按空格时打出向右的子弹，并在子弹离开屏幕消失后删除
"""
class MoveImage:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        self.rect.centerx -= 1

    def blit_me(self):
        self.screen.blit(self.image, self.rect)


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 255))

    center_image = MoveImage(screen)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RIGHT:
                #     if center_image.rect.right + 1 < center_image.screen_rect.right:
                #         center_image.rect.centerx += 1
                # elif event.key == pygame.K_LEFT:
                #     if center_image.rect.left - 1 > 0:
                #         center_image.rect.centerx -= 1
                # elif event.key == pygame.K_UP:
                #     if center_image.rect.top - 1 > 0:
                #         center_image.rect.centery -= 1
                # elif event.key == pygame.K_DOWN:
                #     if center_image.rect.bottom + 1 < center_image.screen_rect.bottom:
                #         center_image.rect.centery += 1
                # else:
                #     continue
                center_image.update()
            elif event.type == pygame.KEYUP:
                pass
            else:
                continue

        # screen.blit(center_image, image_rect)
        """遇到的问题：发现图片移动一直有个黑点在后面，感觉像多个图片，原因是屏幕没更新，图片自我更新之前屏幕也要更新"""
        screen.fill((0, 255, 255))
        center_image.blit_me()
        pygame.display.flip()


start_game()
