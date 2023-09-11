import pygame
import sys
from pygame.locals import *
from random import randint
import os

# ..\python_workspace\Scripts\pyinstaller.exe - F.\dont_touch_android_icon.py --add-binary ".\background.webp;." --add-binary ".\ic_launcher.png;." --add-binary ".\ic_launcher_round.png;." --add-binary ".\replay.png;."


def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


pygame.init()
bg = pygame.image.load(get_resource_path("background.webp"))
bg_position = bg.get_rect()
size = width, height = 800, 500
screen = pygame.display.set_mode(size)

pygame.display.set_caption("别碰到安卓方块图标")

def main():
    class Bird(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(get_resource_path("ic_launcher_round.png"))
            self.rect = self.image.get_rect()
            position = [self.rect.center[0], 235]
            self.rect.center = position
            self.speed_left = [-5, 0]
            self.speed_right = [5, 0]
            self.speed_top = [0, -5]
            self.speed_bottom = [0, 5]

        def move_left(self):
            if self.rect.left - self.speed_left[0] < 0:
                return
            self.rect = self.rect.move(self.speed_left)
            # print(self.rect)

        def move_up(self):
            if self.rect.top - self.speed_top[0] < 0:
                return
            self.rect = self.rect.move(self.speed_top)


        def move_right(self):
            if self.rect.right >= 800:
                return
            self.rect = self.rect.move(self.speed_right)


        def move_bottom(self):
            if self.rect.bottom >= 500:
                return
            self.rect = self.rect.move(self.speed_bottom)


    class Pig(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            y = randint(0, 500)
            position = [800, y]
            self.image = pygame.image.load(get_resource_path("ic_launcher.png"))
            self.rect = self.image.get_rect()
            self.rect.center = position
            self.speed = [-4, 0]

        def move(self):
            self.rect = self.rect.move(self.speed)
            if self.rect.left < 0 or 500 > self.rect.top < 0:
                return

    bird = Bird()
    i = 0
    group = pygame.sprite.Group()
    state = True
    score = 0
    while state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            bird.move_left()
        if key[K_RIGHT]:
            bird.move_right()
        if key[K_UP]:
            bird.move_up()
        if key[K_DOWN]:
            bird.move_bottom()

        screen.blit(bg, bg_position)
        screen.blit(bird.image, bird.rect)

        i = i + 1
        if i % 30 == 0:
            pig = Pig()
            group.add(pig)
            score += 10

        for p in group.sprites():
            p.move()
            if p.rect.right < 0:
                group.remove(p)
            screen.blit(p.image, p.rect)
            if pygame.sprite.collide_mask(bird, p):
                state = False
                pause(score)

        font = pygame.font.SysFont("宋体", 40)  # 大小为20的simhei字体文件（在同一目录下）
        surf = font.render(f"Score : {score}", True, (255, 0, 255))
        screen.blit(surf, (10, 10))
        pygame.display.flip()
        c = pygame.time.Clock()

        c.tick(60)



def pause(score):
    bg_go = pygame.image.load(get_resource_path("background.webp"))
    bg_go_pos = bg_go.get_rect()
    size = widht, height = 800, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GameOver")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        img_src = pygame.image.load(get_resource_path("replay.png"))
        img_src_pos = img_src.get_rect()

        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        left = img_src_pos.left
        right = img_src_pos.right
        top = img_src_pos.top
        bottom = img_src_pos.bottom

        if left + 100 < mouse_pos[0] < right + 100 and top + 185 < mouse_pos[1] < bottom + 185:
            img_src = pygame.image.load(get_resource_path("replay.png"))
            if mouse_press[0]:
                main()
        screen.blit(bg_go, bg_go_pos)
        img_src_pos = img_src.get_rect().center
        screen.blit(img_src, img_src_pos)
        if score != -1:
            font = pygame.font.SysFont("宋体", 60)  # 大小为20的simhei字体文件（在同一目录下）
            surf = font.render(f"Total Score : {score}", True, (0, 255, 255))
            screen.blit(surf, (200, 100))

        pygame.display.flip()


pause(-1)