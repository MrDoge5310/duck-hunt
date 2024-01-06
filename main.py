import random

import pygame
from characters import *
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
bg_image = pygame.image.load('bg-image.png')

ducks_amount = random.randint(1, 3)
ducks = []
print(ducks_amount)
while ducks_amount > 0:
    ducks.append(Sprite(random.randint(0, width-100), height/2, ['duck1.png', 'duck0.png', 'duck2.png', 'duck3.png']))
    ducks_amount -= 1

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    window.blit(bg_image, (0, 0))

    for d in ducks:
        d.move()
        d.animate()
        d.draw(window)
    pygame.display.update()
    clock.tick(10)
pygame.quit()
