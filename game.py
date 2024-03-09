class Game:
    def __init__(self):
        self.score = 0
        self.success = None
        self.total_ducks_killed = 0
        self.ducks_away = 0
        self.killed_ducks = 0

    def restart(self):
        self.__init__()
