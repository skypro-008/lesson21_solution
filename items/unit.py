# todo класс триггеров на изменение состояний игры
from telegram_game.levels.level import coordinates
class Unit:
    def __init__(self, max_hp: int, default_hp, default_defense: int):
        self.max_hp = max_hp
        self.default_hp = default_hp
        self.hp = default_hp
        self.default_defense = default_defense
        self.defense = default_defense
        self.got_key = False
        self.coord = None

    def has_key(self) -> bool:
        return self.got_key

    def set_key(self):
        self.got_key = True

    def _is_alive(self):
        return self.hp > 0

    def get_damage(self, damage: int):
        self.hp -= damage - self.defense
        return self._is_alive()

    def set_coordinates(self, coord: coordinates):
        self.coord = coord

    def get_coordinates(self) -> coordinates:
        return self.coord


class Ghost(Unit):
    def __init__(self, max_hp: int, default_hp, default_defense: int):
        super(Ghost, self).__init__(max_hp=max_hp, default_hp=default_hp, default_defense=default_defense)
        self.name = 'Ghost'
