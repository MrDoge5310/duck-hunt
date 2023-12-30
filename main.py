import pygame
from characters import *
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
bg_image = pygame.image.load('bg-image.png')

d = Sprite(width/2, height/2, 'duck.png')

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(bg_image, (0, 0))
    d.draw(window)

    pygame.display.update()
    clock.tick(30)
pygame.quit()
