import telebot
import config
import os
token_telegram= config.TOKEN
bot = telebot.TeleBot(token_telegram)



con=config.con
#Эта функция просто отправляет сообщение человеку
def MessageTelegramBot(chat_id,message):
    bot.send_message(chat_id,message)

#Эта функция отправляет сообщение всем людям в бд
def MessageAllUsers():
    cur=con.cursor()
    cur.execute(f"SELECT id_user_messenger FROM users where is_login_today=false and id_user_messenger is not NULL;")
    a=cur.fetchall()
    chat_id=''
    for i in a:
        chat_id=i[0]
        bot.send_message(chat_id,"Пожалуйста авторизуйтесь в мессенджере")

    
    



