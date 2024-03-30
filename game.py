import pygame.mixer
import json


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

        self.leaderboard = {}

        self.leaders = []

    def load_leaderboard(self):
        with open('leaderboadr.json', 'r') as file:
            leaderboard_stats = json.load(file)

        i = 0
        self.leaders.clear()
        while i < len(leaderboard_stats):
            self.leaders.append(leaderboard_stats[str(i)])
            i += 1
            if i == 8:
                break
        return self.leaders

    def add_leader(self, no):
        i = 0
        while i < len(self.leaders):
            self.leaderboard[str(i)] = self.leaders[i]
            i += 1

        print(self.leaderboard)

        self.leaderboard[str(no)] = {}
        self.leaderboard[str(no)]["name"] = "Player{}".format(no)
        self.leaderboard[str(no)]["no"] = no + 1
        self.leaderboard[str(no)]["score"] = self.score

        with open('leaderboadr.json', 'w') as file:
            json.dump(self.leaderboard, file)

    def restart(self):
        self.__init__()
