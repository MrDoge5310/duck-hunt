import random

import pygame


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.size = 64
        self.hitbox = pygame.Rect(x, y, self.size, self.size)
        self.frames = filename
        self.image = pygame.image.load(filename[0])
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.frame = 0

        self.dead_images = ['smash_duck.png', 'dead_duck.png']
        self.smash_time = 10

        self.direction = random.choice(['left', 'right'])
        if self.direction == 'right':
            self.vx = random.randint(5, 15)
        if self.direction == 'left':
            self.vx = random.randint(5, 15) * -1
        self.vy = random.randint(5, 15)
        self.canGoAway = False

        self.alive = True

    def draw(self, wnd):
        if self.direction == 'left':
            self.image = pygame.transform.flip(self.image, 1, 0)
        if self.direction == 'right':
            self.image = pygame.transform.flip(self.image, 0, 0)

        if not self.alive:
            if self.smash_time != 0:
                self.image = pygame.image.load(self.dead_images[0])
                self.image = pygame.transform.scale(self.image, (self.size, self.size))
                self.smash_time -= 1
            else:
                self.image = pygame.image.load(self.dead_images[1])
                self.image = pygame.transform.scale(self.image, (self.size, self.size))
                self.vy = 20
        wnd.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def move(self):
        self.hitbox.x += self.vx
        self.hitbox.y += self.vy

        # ограничиваем движение утки пределами игровой области
        if self.hitbox.x < 0:
            if not self.canGoAway:
                self.hitbox.x = 0
                self.vx *= -1
        elif self.hitbox.x > 800 - self.size:
            if not self.canGoAway:
                self.hitbox.x = 800 - self.size
                self.vx *= -1

        if self.hitbox.y < 0:
            if not self.canGoAway:
                self.hitbox.y = 0
                self.canGoAway = True
                self.vy *= -1
        elif self.hitbox.y > 450 - self.size:
            self.hitbox.y = 450 - self.size
            self.vy *= -1

    def animate(self):
        if self.vx > 0:
            self.direction = 'right'
        if self.vx < 0:
            self.direction = 'left'
        if self.frame != len(self.frames) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = pygame.image.load(self.frames[self.frame])
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def kill(self):
        self.alive = False
        self.vx = 0
        self.vy = 0


class Gun:
    def __init__(self):
        self.ammo = 3
        self.reloading = False
        self.reload_time = 3

    def shot(self, x, y, ducks):
        for duck in ducks:
            if duck.hitbox.collidepoint(x, y):
                duck.kill()
