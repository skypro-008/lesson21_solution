from telegram_game.levels.level_1 import Level_1
from telegram_game.levels.level_2 import Level_2
from telegram_game.items.field import Field
from telegram_game.gui import GuiMaker
from telegram_game.exceptions import UnitDied, LevelPassed, InvalidDirection


class GameController:

    def __init__(self):
        self.current_level = Level_2()
        self.field = Field(level=self.current_level)
        self.gui = GuiMaker()

    def process_movement(self, movement: str):
        try:
            self.field.movement(direction=movement)
            return self.make_field_message()
        except InvalidDirection:
            return 'Invalid direction. Direction must be in (left, right, up, down)'
        except UnitDied:
            return 'Unit Died 👻'
        except LevelPassed:
            return 'Yahoo 🎉'

    def make_field_message(self):
        return self.gui.make_telegram_field(field=self.field)
