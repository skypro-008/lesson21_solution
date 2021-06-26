from telegram_game.items.game_item import GameItem
from telegram_game.items.unit import Unit
from telegram_game.exceptions import LevelPassed, UnitDied


class Door(GameItem):
    def __init__(self):
        name = 'Door'
        self.is_locked = True
        super(Door, self).__init__(name=name)

    def step_on(self, unit: Unit):
        self._try_unlock(unit=unit)
        is_opened:bool = self._try_open()
        raise LevelPassed


    def _try_unlock(self, unit: Unit):
        if unit.has_key():
            self.is_locked = False

    def _try_open(self):
        if not self.is_locked:
            return True
        return False


class Key(GameItem):
    def __init__(self):
        name = 'Key'
        super(Key, self).__init__(name=name)

    def step_on(self, unit: Unit):
        unit.set_key()
        return 'Got Key'


class Trap(GameItem):
    def __init__(self, damage: int=2):
        name = 'Trap'
        super(Trap, self).__init__(name=name)
        self.damage = damage

    def step_on(self, unit: Unit):
        unit.get_damage(self.damage)


if __name__ == '__main__':
    door = Door()
    key = Key()
    trap = Trap(damage=1)
    print(door.__dict__)
    print(key.__dict__)
    print(trap.__dict__)
