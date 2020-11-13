import telebot
import config
import psycopg2


token_telegram = config.TOKEN
bot = telebot.TeleBot(token_telegram, threaded = False)



con =config.con



print("telega.py started...")



@ bot.message_handler(commands = ['start'])
def start_message(message):
    print("start")




@ bot.message_handler(content_types = ['text'])
def other(message):
    
    chat_id = message.chat.id
    cur = con.cursor()
    
    

    if len(message.text)>1:
        cur.execute(f"SELECT * FROM users where id_user_messenger={chat_id};")
        usr=cur.fetchone()
        
        if usr==None:#Аккаунт не привязан к коду
            cur.execute(f"SELECT * FROM users where key_messenger=\'{message.text}\';")
            ky=(cur.fetchone())
            
            if ky==None:
                bot.send_message(chat_id,"Неверный ключ")

            else:
                cur.execute(f"SELECT id_user_messenger FROM users where key_messenger=\'{message.text}\';")
                lzh_ky=(cur.fetchone()[0])
                
                if lzh_ky!=None:
                    bot.send_message(chat_id,"Неверный ключ")
                else:
                    cur.execute(f"UPDATE users SET id_user_messenger=\'{chat_id}\' WHERE key_messenger=\'{message.text}\';")

        else:
            cur.execute(f"SELECT is_login_today FROM users where id_user_messenger={chat_id};")
            is_log_day=(cur.fetchone()[0])
            if is_log_day==False:
                cur.execute(f"SELECT key_messenger FROM users where id_user_messenger={chat_id};")
                keycode=cur.fetchone()[0]
                if keycode==message.text:
                    cur.execute(f"UPDATE users SET is_login_today=true WHERE key_messenger='{message.text}';")
                    bot.send_message(chat_id,"Вы успешно авторизовались")
                else:
                    bot.send_message(chat_id,"Неверный код")
            else:
                bot.send_message(chat_id,"Вы уже авторизовались")
            




   
    
    con.commit()
    cur.close()
  
    
    




while True:
    try:
        bot.polling(none_stop = True)
    except:
        continue