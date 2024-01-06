import random

import pygame


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.size = 64
        self.hitbox = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.vx = 5
        self.vy = 5

    def draw(self, wnd):
        wnd.blit(self.image, (self.hitbox.x, self.hitbox.y))

    def move(self):
        self.hitbox.x += self.vx
        self.hitbox.y += self.vy

        # ограничиваем движение утки пределами игровой области
        if self.hitbox.x < 0:
            self.hitbox.x = 0
            self.vx *= -1
        elif self.hitbox.x > 800 - self.size:
            self.hitbox.x = 800 - self.size
            self.vx *= -1

        if self.hitbox.y < 0:
            self.hitbox.y = 0
            self.vy *= -1
        elif self.hitbox.y > 400 - self.size:
            self.hitbox.y = 400 - self.size
            self.vy *= -1
