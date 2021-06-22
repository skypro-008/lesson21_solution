from telegram_game.levels.level import Level, coordinates


class Level_1(Level):
    def __init__(self):
        self.width = 9
        self.height = 3
        self.start_position = coordinates(x=2, y=1)
        self.door_position = coordinates(x=6, y=1)
        self.key_position = coordinates(x=5, y=1)
        self.walls_position = []
        self.traps_position = []

if __name__ == '__main__':
    level = Level_1()
    print(level.__dict__)