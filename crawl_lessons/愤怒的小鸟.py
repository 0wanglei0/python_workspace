import pygame
import sys
from pygame.locals import *
from random import randint


pygame.init()
bg = pygame.image.load("背景图")
bg_position = bg.get_rect()
size = width, height = 1000, 570
screen = pygame.display.set_mode(size)

pygame.display.set_caption("愤怒的小鸟")

def main():
    class Bird(pygame.sprite.Sprite):
        def __init__(self):
            pass


