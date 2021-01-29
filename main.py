import telebot
bot = telebot.TeleBot('1634119418:AAHzc2yueiOxf-MxxzAfLp4t4A5AFBLvwNg')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
         bot.reply_to(message, f'Халоф, я обычный пацанчик с района. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Халоф!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, кентуха')
    else:
        bot.send_message(message.from_user.id, 'Что ты несешь.')

bot.polling()
