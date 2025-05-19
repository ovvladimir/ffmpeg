import telebot


def send_notify(message):
    bot = telebot.TeleBot("token")
    bot.send_message(1791124119, message)
