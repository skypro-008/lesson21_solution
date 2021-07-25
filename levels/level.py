from telegram_game.levels.coordinates import coordinates
from typing import List
from telegram_game.levels.cell import Cell
from telegram_game.items.unit import Ghost


class Level:
    def __init__(self, level_filename: str):
        self.area: List[List[Cell]] = []
        self.level_filename = level_filename
        self.fill_area()

    def fill_area(self):
        file_data = self._read_file()
        for y_coord, line in enumerate(file_data):
            self.area.append(self._process_line(y_coord, line))

    def get_area(self) -> List[List[Cell]]:
        return self.area

    def _process_line(self, y_coord: int, line: str) -> List[Cell]:

        return [self._mark_element(x_coord, y_coord, el) for x_coord, el in enumerate(line)]

    def _mark_element(self, x_coord, y_coord, el: str) -> Cell:
        el_setup = {'W': self._setup_wall,
                    'g': self._setup_grass,
                    'G': self._setup_ghost,
                    'T': self._setup_trap,
                    'K': self._setup_key,
                    'D': self._setup_door}
        return el_setup.get(el, self._setup_grass)(x_coord=x_coord, y_coord=y_coord)

    def _setup_wall(self, **kwargs) -> Cell:
        cell = Cell()
        cell.set_wall()
        return cell

    def _setup_grass(self, **kwargs) -> Cell:
        cell = Cell()
        return cell

    def _setup_ghost(self, **kwargs) -> Cell:
        unit = Ghost(max_hp=10, default_hp=5, default_defense=1)
        unit.set_coordinates(coord = coordinates(x=kwargs['x_coord'], y=kwargs['y_coord']))
        cell = Cell()
        cell.set_unit(unit=unit)
        return cell

    def _setup_trap(self, **kwargs) -> Cell:
        cell = Cell()
        cell.set_trap(damage=2)
        return cell

    def _setup_key(self, **kwargs) -> Cell:
        cell = Cell()
        cell.set_key()
        return cell

    def _setup_door(self, **kwargs) -> Cell:
        cell = Cell()
        cell.set_door()
        return cell

    def _read_file(self, **kwargs):
        _file_data = []
        with open(self.level_filename) as f:
            for line in f:
                _file_data.append(line.strip())
        return _file_data

    def print(self):
        for h in self.area:
            print([f'{cell.name():<6}' for cell in h])


if __name__ == '__main__':
    level = Level(level_filename='/Users/lexicon/TMP/teltgram_game/telegram_game/sample_level.txt')
    level._read_file()
    level.print()
