import telebot
from telegram_game.game_controller import GameController
from typing import Optional

bot = telebot.TeleBot("1716261807:AAGwxdE47AsigAuolVGCGik1NMoiRMelzZY", parse_mode=None)
game: Optional[GameController] = None


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global game
    bot.reply_to(message, "Команды: /right, /left, /up, /down 💀")
    game = GameController()
    bot.reply_to(message, game.make_field_message())


@bot.message_handler(commands=['up'])
def send_welcome(message):
    bot.reply_to(message, game.process_movement(movement='up'))


@bot.message_handler(commands=['down'])
def send_welcome(message):
    bot.reply_to(message, game.process_movement(movement='down'))


@bot.message_handler(commands=['left'])
def send_welcome(message):
    bot.reply_to(message, game.process_movement(movement='left'))


@bot.message_handler(commands=['right'])
def send_welcome(message):
    bot.reply_to(message, game.process_movement(movement='right'))


# @bot.message_handler(func=lambda msg: msg.text.encode("utf-8"))
# def send_something(message):
#     print(message)
bot.polling()
