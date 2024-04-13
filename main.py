import pygame.font
from game import Game
from characters import *

pygame.init()
game = Game()
pygame.mixer_music.load('sound/main_theme.mp3')
pygame.mixer_music.set_volume(0.1)


def draw_menu(wnd):
    pygame.draw.rect(wnd, 'black', score_rect, 0, 15)
    pygame.draw.rect(wnd, 'lime', score_rect, 5, 15)
    score_txt = menu_font.render('Score', 1, 'white')
    wnd.blit(score_txt, (score_rect.x + 15, score_rect.y + 15))
    score_txt = menu_font.render(str(game.score), 1, 'white')
    wnd.blit(score_txt, (score_rect.x + 15, score_rect.y + 15+24))

    bullet_img = pygame.image.load('img/bullet.png')
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
        if index < game.total_ducks_killed:
            pygame.draw.rect(wnd, 'red', ic, 0, 5)
        else:
            pygame.draw.rect(wnd, 'white', ic, 0, 5)


def spawnDucks(ducks_amount):
    temp_ducks = []
    while ducks_amount > 0:
        temp_ducks.append(Sprite(random.randint(0, width-100), height/2, ['img/duck1.png', 'img/duck0.png', 'img/duck2.png', 'img/duck3.png']))
        ducks_amount -= 1
    return temp_ducks


def GameOver(wnd, success, score_):
    play_again_button = pygame.Rect(50, 150, 200, 50)
    exit_button = pygame.Rect(550, 150, 200, 50)
    leaderboard_button = pygame.Rect(275, 250, 250, 50)
    label = pygame.Rect(200, 50, 400, 200)
    wnd.fill('MidnightBlue')

    pygame.draw.rect(wnd, 'black', play_again_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', play_again_button, 5, 15)
    play_text = menu_font.render('Play Again', 1, 'white')
    wnd.blit(play_text, (play_again_button.x + 15, play_again_button.y + 15))

    pygame.draw.rect(wnd, 'black', leaderboard_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', leaderboard_button, 5, 15)
    leaderboard_text = menu_font.render('Leaderboard', 1, 'white')
    wnd.blit(leaderboard_text, (leaderboard_button.x + 15, leaderboard_button.y + 15))

    pygame.draw.rect(wnd, 'black', exit_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', exit_button, 5, 15)
    exit_text = menu_font.render('Exit', 1, 'white')
    wnd.blit(exit_text, (exit_button.x + 15, exit_button.y + 15))

    if success:
        text_label = menu_font.render(f'You WIN! Your score: {score_}', 1, 'white')
    else:
        text_label = menu_font.render(f'You LOOSE! Your score: {score_}', 1, 'white')
    wnd.blit(text_label, (label.x + 15, label.y + 15))

    return [play_again_button, exit_button, leaderboard_button]


def main_menu(wnd):
    play_button = pygame.Rect(100, 100, 200, 75)
    settings_button = pygame.Rect(100, 250, 250, 75)
    exit_button = pygame.Rect(100, 400, 200, 75)
    wnd.fill('MidnightBlue')

    pygame.draw.rect(wnd, 'black', play_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', play_button, 5, 15)
    play_text = menu_font.render('Play', 1, 'white')
    wnd.blit(play_text, (play_button.x + 15, play_button.y + 20))

    pygame.draw.rect(wnd, 'black', settings_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', settings_button, 5, 15)
    settings_text = menu_font.render('Leaderboard', 1, 'white')
    wnd.blit(settings_text, (settings_button.x + 15, settings_button.y + 20))

    pygame.draw.rect(wnd, 'black', exit_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', exit_button, 5, 15)
    exit_text = menu_font.render('Exit', 1, 'white')
    wnd.blit(exit_text, (exit_button.x + 15, exit_button.y + 20))

    return [play_button, settings_button, exit_button]


def leaderboard(wnd):
    exit_button = pygame.Rect(300, 500, 200, 50)
    frame = pygame.Rect(150, 50, 500, 400)
    wnd.fill('MidnightBlue')

    pygame.draw.rect(wnd, 'black', exit_button, 0, 15)
    pygame.draw.rect(wnd, 'lime', exit_button, 5, 15)
    exit_text = menu_font.render('Back', 1, 'white')
    wnd.blit(exit_text, (exit_button.x + 15, exit_button.y + 15))

    pygame.draw.rect(wnd, 'black', frame, 0, 15)
    pygame.draw.rect(wnd, 'lime', frame, 5, 15)

    players = game.load_leaderboard()

    offset = 50
    for player in players:
        line = f"{player['no']}. {player['name']}   Score: {player['score']}"
        line_text = menu_font.render(line, 1, 'white')
        wnd.blit(line_text, (frame.x + 50, frame.y + 15 + offset))
        offset += 50

    return [exit_button]


width = 800
height = 600
window = pygame.display.set_mode((width, height))
bg_image = pygame.image.load('img/bg-image.png')
grass_image = pygame.image.load('img/grass.png')
status = 'menu'

ducks = spawnDucks(random.randint(1, 3))

clock = pygame.time.Clock()
gun = Gun()
dog = Dog(width/2, 380, ['img/dog_noducks.png', 'img/dog_1duck.png', 'img/dog_2ducks.png'])

score_rect = pygame.Rect(width - 175, height - 125, 120, 75)
ammo_rect = pygame.Rect(55, height - 125, 120, 75)
duck_counter = pygame.Rect(200, height - 125, 400, 75)
duck_icons = []

prev_player = game.load_leaderboard()[-1]


i = 0
icon_size = 25
while i < 10:
    duck_icons.append(pygame.Rect(duck_counter.x + i * (icon_size + 12) + 20, duck_counter.y + 25, icon_size, icon_size))
    i += 1
ammo_cords = [(ammo_rect.x + 15, ammo_rect.y + 12),
              (ammo_rect.x + 30+14, ammo_rect.y + 12),
              (ammo_rect.x + 45+28, ammo_rect.y + 12)]

menu_font = pygame.font.Font('Minecraft Rus NEW.otf', 24)

cursor_img_rect = gun.get_rect()

running = True
while running:
    if status == 'menu':
        if not pygame.mixer_music.get_busy():
            pygame.mixer_music.play(-1)
        buttons = main_menu(window)
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if buttons[0].collidepoint(x, y):
                    status = 'game'
                if buttons[1].collidepoint(x, y):
                    status = 'leaderboard'
                if buttons[2].collidepoint(x, y):
                    running = False

    elif status == 'leaderboard':
        buttons = leaderboard(window)
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if buttons[0].collidepoint(x, y):
                    status = 'menu'


    elif status == 'end':
        if pygame.mixer_music.get_busy():
            pygame.mixer_music.stop()
        pygame.mouse.set_visible(True)
        buttons = GameOver(window, game.success, game.score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if buttons[0].collidepoint(x, y):
                    status = 'game'
                    game.restart()
                    ducks = spawnDucks(random.randint(1, 3))
                    gun = Gun()
                if buttons[1].collidepoint(x, y):
                    running = False
                if buttons[2].collidepoint(x, y):
                    status = 'leaderboard'
    else:
        if pygame.mixer_music.get_busy():
            pygame.mixer_music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                gun.shot(x, y, ducks)

        window.blit(bg_image, (0, 0))

        pygame.mouse.set_visible(False)

        cursor_img_rect.center = pygame.mouse.get_pos()
        window.blit(gun.get_img(), cursor_img_rect)

        if len(ducks) == 0:
            gun.ammo = 3
            if game.killed_ducks == 3:
                game.score += 20
                game.killed_ducks = 2
            dog.isVisible = True

        if dog.draw(window, game.killed_ducks):
            ducks = spawnDucks(random.randint(1, 3))
            game.killed_ducks = 0

        for d in ducks:
            d.move()
            d.animate()
            if d.isAway():
                game.score -= 100
                game.ducks_away += 1
                ducks.remove(d)
            if d.isDead():
                game.score += random.randint(100, 201)
                game.total_ducks_killed += 1
                game.killed_ducks += 1
                ducks.remove(d)
            d.draw(window)

        if game.ducks_away >= 3:
            status = 'end'
            game.fail_sound.play(0)
            game.success = False
        if game.total_ducks_killed == 10:
            status = 'end'
            game.add_leader(prev_player["no"])
            game.win_sound.play(0)
            game.success = True

        gun.reload()
        window.blit(grass_image, (0, 110))

        draw_menu(window)

    pygame.display.update()
    clock.tick(10)
pygame.quit()
