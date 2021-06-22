from collections import namedtuple
from abc import ABC
from typing import List, Optional

coordinates = namedtuple('Coordinates', ['x', 'y'])


class Level(ABC):
    width: int
    height: int
    start_position: coordinates
    key_position: coordinates
    door_position: coordinates
    walls_position: List[Optional[coordinates]]
    traps_position: List[Optional[coordinates]]

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_unit_coord(self) -> coordinates:
        return self.start_position

    def set_unit_coord(self, coord: coordinates):
        self.start_position = coord

    def get_key_coord(self) -> coordinates:
        return self.key_position

    def get_door_coord(self) -> coordinates:
        return self.door_position

    def get_walls_coord(self) -> List[Optional[coordinates]]:
        return self.walls_position

    def get_traps_coord(self) -> List[Optional[coordinates]]:
        return self.traps_position