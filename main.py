import telebot
bot = telebot.TeleBot('1634119418:AAHzc2yueiOxf-MxxzAfLp4t4A5AFBLvwNg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()