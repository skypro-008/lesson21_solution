from telegram_game.items.field_items import Grass, Wall
from telegram_game.items.game_item import GameItem
from telegram_game.items.game_items import Door, Key, Trap
from telegram_game.items.unit import Unit
from typing import Union


class Cell:
    obj = None

    def __init__(self):
        self.set_grass()

    def set_grass(self):
        self.obj = Grass()

    def set_wall(self):
        self.obj = Wall()

    def set_unit(self, unit: Unit):
        self.obj = unit

    def remove_unit(self):
        self.obj = Grass()

    def set_door(self):
        self.obj = Door()

    def set_key(self):
        self.obj = Key()

    def set_trap(self, damage=2):
        self.obj = Trap(damage=damage)

    def name(self) -> str:
        return self.obj.name

    def get_obj(self) -> Union[GameItem, Unit]:
        return self.obj
