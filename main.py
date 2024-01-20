import random
from characters import *
pygame.init()


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

ducks = spawnDucks(random.randint(1, 3))

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

    if len(ducks) == 0:
        ducks = spawnDucks(random.randint(1, 3))

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

    gun.reload()
    window.blit(grass_image, (0, 110))
    pygame.display.update()
    clock.tick(10)
pygame.quit()
