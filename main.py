import random

import pygame.font

from characters import *
pygame.init()


def draw_menu(wnd):
    pygame.draw.rect(wnd, 'black', score_rect, 0, 15)
    pygame.draw.rect(wnd, 'lime', score_rect, 5, 15)
    score = menu_font.render('Score', 1, 'white')
    wnd.blit(score, (score_rect.x + 15, score_rect.y + 15))
    score = menu_font.render('00000', 1, 'white')
    wnd.blit(score, (score_rect.x + 15, score_rect.y + 15+24))


def spawnDucks(ducks_amount):
    temp_ducks = []
    while ducks_amount > 0:
        temp_ducks.append(Sprite(random.randint(0, width-100), height/2, ['duck1.png', 'duck0.png', 'duck2.png', 'duck3.png']))
        ducks_amount -= 1
    return temp_ducks


width = 800
height = 600
window = pygame.display.set_mode((width, height))
bg_image = pygame.image.load('bg-image.png')
grass_image = pygame.image.load('grass.png')

ducks_away = 0
killed_ducks = 0

ducks = spawnDucks(random.randint(1, 3))

clock = pygame.time.Clock()
gun = Gun()
dog = Dog(width/2, 380, ['dog_noducks.png', 'dog_1duck.png', 'dog_2ducks.png'])

score_rect = pygame.Rect(width - 175, height - 125, 120, 75)
menu_font = pygame.font.Font('Minecraft Rus NEW.otf', 24)

pygame.mouse.set_visible(False)
cursor_img_rect = gun.get_rect()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            gun.shot(x, y, ducks)

    window.blit(bg_image, (0, 0))

    cursor_img_rect.center = pygame.mouse.get_pos()
    window.blit(gun.get_img(), cursor_img_rect)

    if len(ducks) == 0:
        if killed_ducks == 3:
            killed_ducks = 2
        dog.isVisible = True

    if dog.draw(window, killed_ducks):
        ducks = spawnDucks(random.randint(1, 3))
        killed_ducks = 0

    for d in ducks:
        d.move()
        d.animate()
        if d.isAway():
            ducks_away += 1
            ducks.remove(d)
        if d.isDead():
            killed_ducks += 1
            ducks.remove(d)
        d.draw(window)

    if ducks_away >= 3:
        running = False

    gun.reload()
    window.blit(grass_image, (0, 110))

    draw_menu(window)

    pygame.display.update()
    clock.tick(10)
pygame.quit()
