from abc import ABCMeta, abstractmethod
from telegram_game.items.unit import Unit


class GameItem(metaclass=ABCMeta):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def step_on(self, unit: Unit):
        pass
