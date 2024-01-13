import random
import pygame
from characters import *
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
bg_image = pygame.image.load('bg-image.png')
grass_image = pygame.image.load('grass.png')

ducks_away = 0

ducks_amount = random.randint(1, 3)
ducks = []
while ducks_amount > 0:
    ducks.append(Sprite(random.randint(0, width-100), height/2, ['duck1.png', 'duck0.png', 'duck2.png', 'duck3.png']))
    ducks_amount -= 1

clock = pygame.time.Clock()
gun = Gun()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            gun.shot(x, y, ducks)

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    window.blit(bg_image, (0, 0))

    for d in ducks:
        d.move()
        d.animate()
        if d.isAway():
            ducks_away += 1
            ducks.remove(d)
        if d.isDead():
            ducks.remove(d)
        d.draw(window)

    if ducks_away >= 3:
        running = False

    print(len(ducks))
    gun.reload()
    window.blit(grass_image, (0, 110))
    pygame.display.update()
    clock.tick(10)
pygame.quit()
