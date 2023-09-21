import sys
import time
from random import randint

import pygame

stars = []
image = pygame.image.load("images/alien.bmp")

for row_number in range(3):
    for line_number in range(5):
        x = randint(0, 800)
        y = randint(0, 600)
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        stars.append((image, rect))

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("show starts")
screen.blits(stars)
print("end")
pygame.display.flip()
print("refresh")
time.sleep(3)
print("exit")
sys.exit()
