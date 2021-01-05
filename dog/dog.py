import telebot 
import json
import requests
from telegram import Message 

bot = telebot.TeleBot(TOKEN) # Here instead of TOKEN you should write your own token

# Handler for command /start
@bot.message_handler(commands = ['start'])
def do_welcome(message : Message):   
    bot.send_message(
        message.chat.id, 
        f"Hello my dear {message.from_user.last_name} \n I'm {bot.get_me().first_name} and I was created to give you sweet dogs! \n Type /doggy to get sweet! ")

@bot.message_handler(commands = ['Doggy','dOggy','doGgy','doggY','DOggy','dOGgy','doGGy','dogGY','DoggY','DOGgy','dOGGy','doGGY','DogGY','DOggY','DOGGy','dOGGY','DoGGY','DOgGY','DOGgY','dogy','DOGY','dogi','DOGI','Dogu'])
def wrong_type(message : Message):
    bot.send_message(message.chat.id, 'Hey, did you mean to type: /doggy ?')

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
    extension = f"{url[-3:-1]}{url[-1]}"
    # In these if statements we verify the extension , to understand  which method should we use

    # Check if the extension is a photo
    if(extension == 'jpg' or extension == "png" or extension == "jpeg" or extension == 'JPG' or extension == 'PNG' or extension == 'JPEG'):
        bot.send_photo(message.chat.id, url)
    # Check if the extension is a gif 
    if(extension == 'gif' or extension == 'GIF' or extension == 'webm' or extension == 'WEBM'):
        bot.send_animation(message.chat.id,url)
    
    # And the last extension , which isn't a photo nor a gif, is mp4(video extension) 
    else:
        bot.send_video(message.chat.id, url)


print("Polling is on...")
bot.polling()
