import telebot
import os

from config import token
from logic import gen_pass
from random import choice

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['password'])
def make_pass(message):
    bot.send_message(message.chat.id, str(gen_pass(7)))

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


@bot.message_handler(commands=["dream"])
def send_photo(message):
    image_rand = choice(os.listdir('image'))
    with open(f'image/{image_rand}', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=["cat"])
def send_photo(message):
    image_rand = choice(os.listdir('cats'))
    with open(f'cats/{image_rand}', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    


bot.infinity_polling()
