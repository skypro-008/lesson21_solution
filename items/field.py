from telegram_game.levels.level import Level
from telegram_game.items.field_items import Grass, Wall, Shadow
from telegram_game.items.game_items import Door, Key, Trap
from telegram_game.items.unit import Ghost
from telegram_game.levels.level import coordinates
from telegram_game.items.game_item import GameItem
from telegram_game.items.unit import Unit
from typing import Optional
from telegram_game.exceptions import InvalidDirection, UnitDied, LevelPassed


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

    def get_obj(self) -> GameItem:
        return self.obj


class Field:
    field = []
    unit: Optional[Unit] = None

    def __init__(self, level: Level):
        self.level = level
        self._clear_field()
        self._make_field()
        self._setup()

    def movement(self, direction: str):
        if direction not in {'up', 'down', 'left', 'right'}:
            raise InvalidDirection(f'{direction=}')
        directions ={'up': self.move_unit_up,
                     'down': self.move_unit_down,
                     'left': self.move_unit_left,
                     'right': self.move_unit_right,
                     }
        directions[direction]()

    def move_unit_up(self):
        unit_coord = self.unit.get_coordinates()
        new_coord = coordinates(x=unit_coord.x, y=unit_coord.y + 1)
        self._process_movement(new_coord, unit_coord)

    def move_unit_down(self):
        unit_coord = self.unit.get_coordinates()
        new_coord = coordinates(x=unit_coord.x, y=unit_coord.y - 1)
        self._process_movement(new_coord, unit_coord)

    def move_unit_right(self):
        unit_coord = self.unit.get_coordinates()
        new_coord = coordinates(x=unit_coord.x + 1, y=unit_coord.y)
        self._process_movement(new_coord, unit_coord)

    def move_unit_left(self):
        unit_coord = self.unit.get_coordinates()
        new_coord = coordinates(x=unit_coord.x - 1, y=unit_coord.y)
        self._process_movement(new_coord, unit_coord)

    def _process_movement(self, new_coord, unit_coord):
        if self._check_ability_to_move(coord=new_coord):
            old_cell = self._get_cell(coord=unit_coord)
            new_cell = self._get_cell(coord=new_coord)
            old_cell.remove_unit()
            new_cell.get_obj().step_on(unit=self.unit)
            # todo обработка триггеров тут
            new_cell.set_unit(unit=self.unit)

    def _check_ability_to_move(self, coord) -> bool:
        cell = self._get_cell(coord=coord)
        return not cell.name() == 'Wall'

    def _clear_field(self):
        self.field = []
        self.unit = None

    def _make_field(self):
        for h in range(self.level.get_height()):
            self.field.append(self._make_empty_line())
        self._make_horizontal_border(idx=0)
        self._make_horizontal_border(idx=-1)
        self._make_vertical_border(idx=0)
        self._make_vertical_border(idx=-1)

    def _setup(self):
        self._set_unit()
        self._set_key()
        self._set_door()
        self._set_walls()
        self._set_traps()

    def _make_empty_line(self) -> list:
        line = [Cell() for _ in range(self.level.get_width())]
        return line

    def _make_horizontal_border(self, idx: int):
        for cell in self.field[idx]:
            cell.set_wall()

    def _make_vertical_border(self, idx: int):
        for line in self.field:
            line[idx].set_wall()

    def _set_unit(self):
        unit_coord = self.level.get_unit_coord()
        ghost = Ghost(max_hp=10, default_hp=5, default_defense=0)
        ghost.set_coordinates(coord=unit_coord)
        cell = self._get_cell(coord=unit_coord)
        cell.set_unit(unit=ghost)
        self.unit = ghost

    def _set_door(self):
        coord = self.level.get_door_coord()
        cell = self._get_cell(coord=coord)
        cell.set_door()

    def _set_key(self):
        coord = self.level.get_key_coord()
        cell = self._get_cell(coord=coord)
        cell.set_key()

    def _set_walls(self):
        for coord in self.level.get_walls_coord():
            self._set_wall(coord=coord)

    def _set_traps(self):
        for coord in self.level.get_traps_coord():
            self._set_trap(coord=coord)

    def _set_wall(self, coord: coordinates):
        cell = self._get_cell(coord=coord)
        cell.set_wall()

    def _set_trap(self, coord: coordinates):
        cell = self._get_cell(coord=coord)
        cell.set_trap()

    def _get_cell(self, coord: coordinates) -> Cell:
        return self.field[coord.y][coord.x]

    def print(self):
        for h in self.field:
            print([f'{cell.name():<6}' for cell in h])


if __name__ == '__main__':
    from telegram_game.levels.level_1 import Level_1

    level1 = Level_1()
    field = Field(level=level1)
    field.move_unit_right()
    field.move_unit_up()
    field.print()
