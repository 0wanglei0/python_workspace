import sys

import pygame
from pygame.sprite import Sprite, Group

"""
1.雨滴
rect y

check_edge

create多个

"""


class Rain(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x = self.rect.width
        self.y = self.rect.height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.fleet_drop_speed = 3
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

        screen.fill((230, 230, 230))
        rains.draw(screen)
        pygame.display.flip()


start_rain()
