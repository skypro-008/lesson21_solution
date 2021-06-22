from telegram_game.items.game_item import GameItem
from telegram_game.items.unit import Unit


class Fielditem(GameItem):
    pass


class Grass(Fielditem):
    def __init__(self):
        name = 'Grass'
        super(Grass, self).__init__(name=name)

    def step_on(self, unit: Unit):
        pass


class Wall(Fielditem):
    def __init__(self):
        name = 'Wall'
        super(Wall, self).__init__(name=name)

    def step_on(self, unit: Unit):
        pass


class Shadow(Fielditem):
    def __init__(self):
        name = 'Shadow'
        super(Shadow, self).__init__(name=name)

    def step_on(self, unit: Unit):
        pass
