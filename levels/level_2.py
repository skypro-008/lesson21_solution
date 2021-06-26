from telegram_game.levels.level import Level, coordinates


class Level_2(Level):
    def __init__(self):
        self.width = 15
        self.height = 6
        self.start_position = coordinates(x=2, y=1)
        self.door_position = coordinates(x=6, y=1)
        self.key_position = coordinates(x=5, y=1)
        self.walls_position = []
        self.traps_position = [coordinates(x=2, y=2),
                               coordinates(x=3, y=2),
                               coordinates(x=4, y=2),
                               coordinates(x=5, y=2),
                               coordinates(x=6, y=2),
                               coordinates(x=7, y=2), ]

if __name__ == '__main__':
    level = Level_2()
    print(level.__dict__)