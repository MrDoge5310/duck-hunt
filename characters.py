import pygame


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.size = 64
        self.hitbox = pygame.Rect(x, y, self.size, self.size)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def draw(self, wnd):
        wnd.blit(self.image, (self.hitbox.x, self.hitbox.y))
