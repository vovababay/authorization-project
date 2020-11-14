import telebot
import config
import random

from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton("Сгенерировать код")
    item4 = types.KeyboardButton("Кто-то вошел(симуляция)")

    markup.add(item3, item4)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, - бот от которого ты будешь получать код подверждения и уведомления.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == "private":

    	if message.text == 'Кто-то вошел(симуляция)': 

    		markup = types.InlineKeyboardMarkup(row_width=2)
    		item1 = types.InlineKeyboardButton('Это я.', callback_data='no_alarm')
    		item2 = types.InlineKeyboardButton('Это не я!!!', callback_data='alarm')


    		markup.add(item1,item2)

    		bot.send_message(message.chat.id, 'В ваш аккаунт файлового хранилища производится вход. Это вы?', reply_markup=markup) 		

    	elif message.text == 'Сгенерировать код':
    		def create_password():
    			chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    			password =''
    			for i in range(5):
    				password += random.choice(chars)
    			return password
    		password_message=create_password()
    		bot.send_message(message.chat.id, password_message)

    	else:
    		bot.send_message(message.chat.id, 'Я не знаю что тебе ответить')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'no_alarm':
				bot.send_message(call.message.chat.id, 'Фух😳, а я уже распереживался. Удачной работы😉')
			elif call.data == 'alarm':
				bot.send_message(call.message.chat.id, 'Ах он 🤬, выполняю заморозку аккаунта🥶 и отправляю уведомление админу🆘😤❗️❗️❗️')

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кто-то вошел(симуляция)",
				reply_markup=None)

			bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
				text='Понял вас.')

	except Exception as e:
		print(repr(e))

#RUN
bot.polling(none_stop=True)