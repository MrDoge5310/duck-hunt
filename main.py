import random
import pygame.font

from characters import *
pygame.init()


def draw_menu(wnd):
    pygame.draw.rect(wnd, 'black', score_rect, 0, 15)
    pygame.draw.rect(wnd, 'lime', score_rect, 5, 15)
    score_txt = menu_font.render('Score', 1, 'white')
    wnd.blit(score_txt, (score_rect.x + 15, score_rect.y + 15))
    score_txt = menu_font.render(str(score), 1, 'white')
    wnd.blit(score_txt, (score_rect.x + 15, score_rect.y + 15+24))

    bullet_img = pygame.image.load('bullet.png')
    pygame.draw.rect(wnd, 'black', ammo_rect, 0, 15)
    pygame.draw.rect(wnd, 'lime', ammo_rect, 5, 15)
    ammo = menu_font.render('Shot', 1, 'white')

    i = 0
    while i < gun.ammo:
        wnd.blit(bullet_img, ammo_cords[i])
        i += 1

    wnd.blit(ammo, (ammo_rect.x + 15, ammo_rect.y + 15+24))

    pygame.draw.rect(wnd, 'black', duck_counter, 0, 15)
    pygame.draw.rect(wnd, 'lime', duck_counter, 5, 15)

    for ic in duck_icons:
        index = duck_icons.index(ic)
        if index < total_ducks_killed:
            pygame.draw.rect(wnd, 'red', ic, 0, 5)
        else:
            pygame.draw.rect(wnd, 'white', ic, 0, 5)


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
status = 'menu'

ducks_away = 0
killed_ducks = 0

ducks = spawnDucks(random.randint(1, 3))

clock = pygame.time.Clock()
gun = Gun()
dog = Dog(width/2, 380, ['dog_noducks.png', 'dog_1duck.png', 'dog_2ducks.png'])

score = 0
total_ducks_killed = 0

score_rect = pygame.Rect(width - 175, height - 125, 120, 75)
ammo_rect = pygame.Rect(55, height - 125, 120, 75)
duck_counter = pygame.Rect(200, height - 125, 400, 75)
duck_icons = []


def main_menu(wnd):
    play_button = pygame.Rect(100, 200, 200, 75)
    settings_button = pygame.Rect(100, 400, 200, 75)
    exit_button = pygame.Rect(100, 600, 200, 75)

    isMenu = True
    while isMenu:
        wnd.fill('MidnightBlue')

        pygame.draw.rect(wnd, 'black', play_button, 0, 15)
        pygame.draw.rect(wnd, 'lime', play_button, 5, 15)
        play_text = menu_font.render('Play', 1, 'white')
        wnd.blit(play_text, (play_button.x + 15, play_button.y + 15))

        pygame.draw.rect(wnd, 'black', settings_button, 0, 15)
        pygame.draw.rect(wnd, 'lime', settings_button, 5, 15)
        settings_text = menu_font.render('Play', 1, 'white')
        wnd.blit(settings_text, (settings_button.x + 15, settings_button.y + 15))

        pygame.draw.rect(wnd, 'black', exit_button, 0, 15)
        pygame.draw.rect(wnd, 'lime', exit_button, 5, 15)
        exit_text = menu_font.render('Play', 1, 'white')
        wnd.blit(exit_text, (exit_button.x + 15, exit_button.y + 15))

        for event_ in pygame.event.get():
            if event_.type == pygame.MOUSEBUTTONDOWN and event_.button == 1:
                x_, y_ = pygame.mouse.get_pos()
                if play_button.collidepoint(x_, y_):
                    break
        pygame.display.update()
        clock.tick(60)


i = 0
icon_size = 25
while i < 10:
    duck_icons.append(pygame.Rect(duck_counter.x + i * (icon_size + 12) + 20, duck_counter.y + 25, icon_size, icon_size))
    i += 1
ammo_cords = [(ammo_rect.x + 15, ammo_rect.y + 12),
              (ammo_rect.x + 30+14, ammo_rect.y + 12),
              (ammo_rect.x + 45+28, ammo_rect.y + 12)]

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
        gun.ammo = 3
        if killed_ducks == 3:
            score += 20
            killed_ducks = 2
        dog.isVisible = True

    if dog.draw(window, killed_ducks):
        ducks = spawnDucks(random.randint(1, 3))
        killed_ducks = 0

    for d in ducks:
        d.move()
        d.animate()
        if d.isAway():
            score -= 100
            ducks_away += 1
            ducks.remove(d)
        if d.isDead():
            score += random.randint(100, 201)
            total_ducks_killed += 1
            killed_ducks += 1
            ducks.remove(d)
        d.draw(window)

    if ducks_away >= 3:
        running = False
    if total_ducks_killed == 10:
        running = False

    gun.reload()
    window.blit(grass_image, (0, 110))

    draw_menu(window)

    pygame.display.update()
    clock.tick(10)
pygame.quit()
