import telebot 
import json
import requests
from telegram import Message 


bot = telebot.TeleBot(token = "TOKEN") # Here instead of TOKEN you should write your own token


# Handler for command /start
@bot.message_handler(commands = ['start'])
def do_welcome(message : Message):   
    bot.send_message(
        message.chat.id, 
        f"Hello my dear {message.from_user.first_name} \n I'm {bot.get_me().first_name} and I was created to give you sweet dogs! \n Type /doggy to get sweet! ")



# Get images from random.dog to use them in our bot as a response to command  /doggy
def get_url():
    response = requests.get("https://random.dog/woof.json")
    content = json.loads(response.text) 
    url = content['url'] 
    return url



# Handler for command /doggy
# Instead of doggy you can write another command which you like
@bot.message_handler(commands = ['doggy'])
def do_doggy(message : Message):
    url = get_url()   
    # Here we get the extension of the file ( .jpg , .png etc.)


    temp = url.split(sep = '.')
    extension = temp[-1]
    print(extension)


    # In these if statements we verify the extension , to understand  which method should we use
    # Check if the extension is a photo
    if(extension.lower() == 'jpeg' or extension.lower() == "png" or extension.lower() == "jpg"):
        bot.send_photo(message.chat.id, url)


    
    # Check if the extension is a gif 
    if(extension.lower() == 'gif'):
        bot.send_animation(message.chat.id,url)


    # And the last extension , which isn't a photo nor a gif, is mp4(video extension) 
    if(extension.lower() == 'mp4' or extension.lower() == 'webm'):
        bot.send_video(message.chat.id, url)


print("Polling is off...")
bot.polling()
