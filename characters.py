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
        self.vx = random.randint(6, 10)
        self.vy = random.randint(6, 10)
        self.canGoAway = False

    def draw(self, wnd):
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
        elif self.hitbox.y > 400 - self.size:
            self.hitbox.y = 400 - self.size
            self.vy *= -1

    def animate(self):
        if self.frame != len(self.frames) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.image = pygame.image.load(self.frames[self.frame])
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

