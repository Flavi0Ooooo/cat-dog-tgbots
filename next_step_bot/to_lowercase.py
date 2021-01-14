import telebot 
from telegram import Message

API_TOKEN = '1550470196:AAGnA1jL6Giv4b7cHqEahnqZeZV_h8mB60Y'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def send_welcome(message : Message):
    try:
        msg = bot.send_message(message.chat.id, "SCRIE TOP 1 FACT DESPRE UCRAINA DUPA PAREREA TA!")
        bot.register_next_step_handler(msg,to_lower_case)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def to_lower_case(message : Message):
    to_lower_case_message = message.text
    bot.send_message(message.chat.id, to_lower_case_message.lower())

bot.polling()