import json
import requests
import telebot
import random
import telepot
import os
from telebot.types import Message
from pprint import pprint

TOKEN = '475716125:AAFeMVoiigDF8LjEkjh54BADNuNTBRPf3EY'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
TelegramBot = telepot.Bot(TOKEN)
print(TelegramBot.getMe())
print(TelegramBot.getUpdates())

telegramUId = 257017756
telegramXUId = 341982379

payload = {}
payload['chat_id'] = -301227966
# payload['text'] = 'ola-la'
smiles = ['😶', '😐', '😌', '😊', '🙂', '😀', '😄', '😁', '😆', '😃']

r = requests.post(URL + 'sendMessage', payload)

payload['chat_id'] = -301227966
payload['longitude'] = '78.785194'
payload['latitude'] = '35.834421'
r = requests.post(URL + 'sendLocation', payload)

bot = telebot.TeleBot(TOKEN)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id == telegramUId:
        bot.reply_to(message, "Hello my master, how are you doing?")
    else:
        bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    if message.text == "Hi":
        bot.reply_to(message, "Hi yourself!")
    bot.reply_to(message, random.choice(smiles))
    sti = open(ROOT_DIR + '/Porto.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    print(TelegramBot.getMe())
    print(TelegramBot.getUpdates())


bot.polling()