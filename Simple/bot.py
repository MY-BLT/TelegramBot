from telebot import TeleBot, types
from dotenv import load_dotenv
import os
from pathlib import Path

# load the path for .env
env_path = Path(__file__).resolve().parent.parent / ".env"

# load the .env file
load_dotenv(dotenv_path=env_path)

# The token gotten from botfather in telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

# The token that is got from bot father
bot = TeleBot(BOT_TOKEN)
# The order of running the codes are like you write in the editor

@bot.message_handler(commands=["start", "help"])
def hello(message):
    # Reply keyboards:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Info")
    btn2 = types.KeyboardButton("Help")
    btn3 = types.KeyboardButton("README")
    
    keyboard.add(btn1, btn2, btn3)
    if message.text == "/start":
        bot.send_message(message.chat.id,  "Welcom to my bot.", reply_markup=keyboard)
        bot.send_message(message.from_user.id, f"{message.from_user.first_name} start @MY_BLT_bot.\n@{message.from_user.username}")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "This bot is for test you.")

# In line keyboards:
@bot.message_handler(func= lambda m : "info" in m.text.lower())
def Info_message(message):
    markup = types.InlineKeyboardMarkup(row_width= 2)
    btn1 = types.InlineKeyboardButton("start", callback_data= "/start") 
    btn2 = types.InlineKeyboardButton("help", callback_data= "/help", )

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Choose one option:", reply_markup= markup)
       
@bot.message_handler(func= lambda m : "info" in m.text.lower())
def send_option_message(message):
    bot.send_message(message.chat.id, "1./start\n2./help")

bot.message_handler(func= lambda m : "help" in m.text.lower())
def send_option_message(message):
    if message.text.lower() == "help":
        hello("/help")
    
@bot.message_handler(regexp=r"\byasin\b", content_types=["text"])
def send_yasin_message(message):
    bot.send_message(message.chat.id, "Yasin is a great guy!")

@bot.message_handler(regexp=r"^\/")
def send_unknown_command(message):
    bot.send_message(message.chat.id, "Please use /start or /help to get information.")

@bot.message_handler(chat_types=["private"])
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

# we can use fuctions like lambda in input of message_handler
bot.polling()