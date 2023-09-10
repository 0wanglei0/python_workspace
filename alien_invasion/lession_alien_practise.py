import sys

import pygame


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 255))

    center_image = pygame.image.load("images/ship.bmp")
    center_image.fill((255, 0, 255))
    center_image.set_alpha(0)
    #
    # screen.fill(center_image.)
    image_rect = center_image.get_rect()
    screen_rect = screen.get_rect()

    image_rect.centerx = screen_rect.centerx
    image_rect.centery = screen_rect.centery
    screen.blit(center_image, image_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


start_game()
