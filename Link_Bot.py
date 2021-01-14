import telebot
from telegram import Message


bot = telebot.TeleBot(token = 'TOKEN')

@bot.message_handler(commands = ['Romana'])
def link_romana(message : Message):
    bot.send_message(message.chat.id , 'https://meetingsemea28.webex.com/join/pr1632755058')
    
    
@bot.message_handler(commands = ['Istoria'])
def link_istoria(message : Message):
    bot.send_message(message.chat.id , 'https://us04web.zoom.us/j/3912310260?pwd=eUpLU1pFU3ZyQ016RmpRVy9EcFVOZz09')
    
    
print('Polling is on')
bot.polling()
    
    
    
