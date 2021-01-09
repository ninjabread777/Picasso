import telebot
import logging
logger = telebot.logger

logging.basicConfig(format='%(asctime)s-%(message)s',
                    level=logging.INFO,
                    filename='bot.log')
boss=150962695
bot = telebot.TeleBot('1531646920:AAGC30IxLcb1S91rk3Sgw8HISwf9f-AJ5LE')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"тут типо меню для шаблонов:", reply_markup=markup)
from telebot import types

# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('url1')
itembtn2 = types.KeyboardButton('url1')
itembtn3 = types.KeyboardButton('url1')
itembtn4 = types.KeyboardButton('url1')
itembtn5 = types.KeyboardButton('url1')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        logging.info(message.text)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
        logging.info(message.text)
    elif message.text.lower() == 'dick':
        bot.forward_message(boss, message.chat.id, message.message_id)
        x = message.from_user.username + ': ' + message.text
        logging.info(x)
    elif message.text.lower() != '':
        x=message.from_user.username+': '+ message.text
        logging.info(x)


@bot.callback_query_handler(func=lambda call: True)
def  test_callback(call):
    logger.info(call)
bot.polling()