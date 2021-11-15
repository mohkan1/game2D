import pygame
from pygame.locals import *

pygame.init()


screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

#load images
sun_image = pygame.image.load("img/sun.png")
sky_image = pygame.image.load("img/sky.png")

run = True
while run:
    screen.blit(sky_image, (0,0))
    screen.blit(sun_image, (100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()