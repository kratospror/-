import telebot
from telebot import types


bot = telebot.TeleBot('6072348335:AAFX1FM1GTfzkOJBkU5B30vswcwdH-Wvu2Q')

@bot.message_handler (commands=['start'])
def start(message):
     mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
     bot.send_message(message.chat.id, mess, parse_mode='html')

#@bot.message_handler()
## if message.text == "Привет":
        #bot.send_message(message.chat.id, "Вас приветствует бот grogu", parse_mode='html')
     #elif message.text == "id":
      #  bot.send_message(message.chat.id, f"This is id: {message.from_user.id}", parse_mode='html')
     #elif message.text == 'Фото':
       # photo = open('photoPS4/ps4.png', 'rb')
        # bot.send_photo(message.chat.id, photo)
     #else:
      # bot.send_message(message.chat.id, "I am not a speak", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Это то что мне нужно')

@bot.message_handler(commands=['website'])
def website(message):
    read = types.InlineKeyboardMarkup()
    read.add(types.InlineKeyboardButton('Необходимо перейти на веб сайт', url='https://vk.com/feed'))
    bot.send_message(message.chat.id, 'ПЕРЕЙТИ на САЙт', reply_markup=read)

@bot.message_handler(commands=['help'])
def website(message):
    read = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Website')
    start = types. KeyboardButton('Start')
    read.add(website, start)
    #read.add(types.InlineKeyboardButton('Необходимо перейти на веб сайт', url='https://vk.com/feed'))
    bot.send_message(message.chat.id, 'ПЕРЕЙТИ на САЙт', reply_markup=read)



bot.polling(none_stop=True)


