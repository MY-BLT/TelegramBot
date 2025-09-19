from telebot import TeleBot, types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_bot(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn_st = types.InlineKeyboardButton(text="Student", callback_data="student")
    btn_te = types.InlineKeyboardButton(text="Teacher", callback_data="teacher")
    btn_pr = types.InlineKeyboardButton(text="Professor", callback_data="professor")
    
    markup.add(btn_st, btn_te, btn_pr)
    
    bot.send_message(message.chat.id, f"Welcome {message.from_user.username}", reply_markup=markup)

@bot.callback_query_handler(func= lambda call : True)
def send_spec_message(call):
    if call.data == "student":
        bot.answer_callback_query(call.id, text="You logged in form of student")
    elif call.data == "teacher":
        bot.answer_callback_query(call.id, text="You logged in form of teacher")
    elif call.data == "professor":
        bot.answer_callback_query(call.id, text="You logged in form of professor")
    else:
        bot.answer_callback_query(call.id, text="Welcome!")

bot.polling()