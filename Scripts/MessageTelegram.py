import telebot
import config
import os
token_telegram= config.TOKEN
bot = telebot.TeleBot(token_telegram)




con=config.con

def MessageTelegramBot(chat_id,message):
    bot.send_message(chat_id,message)


def MessageAllUsers():
    cur=con.cursor()
    cur.execute(f"SELECT id_user_messenger FROM users where is_login_today=false and id_user_messenger is not NULL;")
    a=cur.fetchall()
    chat_id=''
    for i in a:
        chat_id=i[0]
        bot.send_message(chat_id,"Пожалуйста авторизуйтесь в мессенджере")

    
def MessegeLock(login,message):
    cur = con.cursor()
    cur.execute(f"SELECT id_user_messenger FROM users WHERE login='{login}';")
    id_user = cur.fetchone()[0]
    bot.send_message(id_user,message)



