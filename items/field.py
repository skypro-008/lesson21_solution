from telegram_game.levels.level import Level
from telegram_game.items.unit import Unit
from telegram_game.levels.coordinates import coordinates
from typing import Optional
from telegram_game.levels.cell import Cell
from telegram_game.exceptions import InvalidDirection


class Field:
    field = []
    unit: Optional[Unit] = None

    def __init__(self, level: Level):
        self.level = level
        self._clear_field()
        self._make_field()


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
        new_coord = coordinates(x=unit_coord.x, y=unit_coord.y - 1)
        self._process_movement(new_coord, unit_coord)

    def move_unit_down(self):
        unit_coord = self.unit.get_coordinates()
        new_coord = coordinates(x=unit_coord.x, y=unit_coord.y + 1)
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
            new_cell.get_obj().step_on(unit=self.unit)

            old_cell.remove_unit()
            new_cell.set_unit(unit=self.unit)
            self.unit.set_coordinates(coord=new_coord)

    def _check_ability_to_move(self, coord) -> bool:
        cell = self._get_cell(coord=coord)
        return not cell.name() == 'Wall'

    def _clear_field(self):
        self.field = []
        self.unit = None

    def _make_field(self):
        self.field = self.level.get_area()
        units = [x for sub in self.field for x in sub if isinstance(x.get_obj(), Unit)]
        self.unit = units[0].get_obj()

    # def _set_unit(self):
    #     unit_coord = self.level.get_unit_coord()
    #     ghost = Ghost(max_hp=10, default_hp=5, default_defense=0)
    #     ghost.set_coordinates(coord=unit_coord)
    #     cell = self._get_cell(coord=unit_coord)
    #     cell.set_unit(unit=ghost)
    #     self.unit = ghost
    #
    # def _set_door(self):
    #     coord = self.level.get_door_coord()
    #     cell = self._get_cell(coord=coord)
    #     cell.set_door()
    #
    # def _set_key(self):
    #     coord = self.level.get_key_coord()
    #     cell = self._get_cell(coord=coord)
    #     cell.set_key()
    #
    # def _set_walls(self):
    #     for coord in self.level.get_walls_coord():
    #         self._set_wall(coord=coord)
    #
    # def _set_traps(self):
    #     for coord in self.level.get_traps_coord():
    #         self._set_trap(coord=coord)
    #
    # def _set_wall(self, coord: coordinates):
    #     cell = self._get_cell(coord=coord)
    #     cell.set_wall()
    #
    # def _set_trap(self, coord: coordinates):
    #     cell = self._get_cell(coord=coord)
    #     cell.set_trap()
    #
    def _get_cell(self, coord: coordinates) -> Cell:
        return self.field[coord.y][coord.x]

    def get_field(self):
        return self.field

    def print(self):
        for h in self.field:
            print([f'{cell.name():<6}' for cell in h])


if __name__ == '__main__':
    level1 = Level(level_filename='/Users/lexicon/TMP/teltgram_game/telegram_game/sample_level.txt')
    field = Field(level=level1)
    # field.move_unit_left()
    field.move_unit_down()
    field.move_unit_down()
    field.move_unit_up()
    # field.move_unit_right()
    field.print()
