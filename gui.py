from telegram_game.items.field import Field
from telegram_game.levels.cell import Cell


class GuiMaker:
    telegram_mapping={
        'Wall': '🔲',
        'Grass': '⬜️',
        'Ghost': '👻',
        'Key': '🗝',
        'Door': '🚪',
        'Trap': '💀',

    }

    def make_telegram_field(self, field: Field):
        message = []
        for h in field.get_field():
            message.append(''.join([self.telegram_mapping[cell.name()] for cell in h]))
        return '\n'.join(message)