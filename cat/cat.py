import telebot 
import json
import requests
from telegram import Message 

bot = telebot.TeleBot(token = "TOKEN") # Here instead of token you should write your token

# Handler for command /start
@bot.message_handler(commands = ['start'])
def do_welcome(message : Message):   
    bot.send_message(
        message.chat.id, 
        f"Hello my dear {message.from_user.last_name} \n I'm {bot.get_me().first_name} and I was created to give you sweet cats! \n Type /catty to get sweet! ")

# Get images from random.dog to use them in our bot as a response to command  /catty
def get_url():
    response = requests.get("https://api.thecatapi.com/v1/images/search")  
    contents = json.loads(response.text)
    url = None 
    for content in contents:
        url = content['url']
    return url

# Handler for command cats
# Instead of cats you can write another, which you like , or simply just leave the command as it is  
@bot.message_handler(commands = ['cats'])
def do_catty(message : Message):
    url = get_url()   
    bot.send_photo(message.chat.id,  url)

print("Polling is on...")
bot.polling()   
