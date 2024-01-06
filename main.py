import pygame
from characters import *
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
bg_image = pygame.image.load('bg-image.png')

d = Sprite(width/2, height/2, ['duck0.png', 'duck1.png', 'duck2.png'])

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    window.blit(bg_image, (0, 0))

    d.move()
    d.animate()

    d.draw(window)
    pygame.display.update()
    clock.tick(15)
pygame.quit()
