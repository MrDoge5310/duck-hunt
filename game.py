import pygame.mixer


class Game:
    def __init__(self):
        self.score = 0
        self.success = None
        self.total_ducks_killed = 0
        self.ducks_away = 0
        self.killed_ducks = 0

        self.win_sound = pygame.mixer.Sound('sound/gameover_win.mp3')
        self.fail_sound = pygame.mixer.Sound('sound/gameover_fail.mp3')
        self.win_sound.set_volume(0.2)
        self.fail_sound.set_volume(0.2)

    def restart(self):
        self.__init__()
