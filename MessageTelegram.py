import telebot
import config
import os
token_telegram= config.TOKEN
bot = telebot.TeleBot(token_telegram)


def MessageTelegramBot(chat_id,message):
    bot.send_message(chat_id,message)

